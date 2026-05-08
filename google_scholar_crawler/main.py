from __future__ import annotations

import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.parse import parse_qs, urljoin, urlparse
from urllib.request import Request, urlopen

from bs4 import BeautifulSoup


ROOT = Path(__file__).resolve().parents[1]
RESULTS_DIR = Path(__file__).resolve().parent / "results"
PROFILE_URL = "https://scholar.google.com/citations"
FALLBACK_USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/124.0 Safari/537.36"
)


def clean_text(value: str | None) -> str:
    value = re.sub(r"\s+", " ", value or "").strip()
    return re.sub(r"\s+([,;:])", r"\1", value)


def parse_int(value: str | None) -> int | None:
    if not value:
        return None
    match = re.search(r"[\d,]+", value)
    if not match:
        return None
    return int(match.group(0).replace(",", ""))


def read_scholar_id() -> str:
    scholar_id = clean_text(os.environ.get("GOOGLE_SCHOLAR_ID"))
    if scholar_id:
        return scholar_id

    config = ROOT / "_config.yml"
    if config.exists():
        match = re.search(r"scholar\.google\.com/citations\?user=([^&\"'\s]+)", config.read_text())
        if match:
            return match.group(1)

    raise RuntimeError(
        "GOOGLE_SCHOLAR_ID is not set and no Scholar user id was found in _config.yml."
    )


def fetch_profile_html(scholar_id: str) -> str:
    url = f"{PROFILE_URL}?user={scholar_id}&hl=en&pagesize=100"
    request = Request(
        url,
        headers={
            "User-Agent": os.environ.get("GOOGLE_SCHOLAR_USER_AGENT", FALLBACK_USER_AGENT),
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.9",
        },
    )

    try:
        with urlopen(request, timeout=30) as response:
            html = response.read().decode("utf-8", errors="replace")
    except HTTPError as error:
        raise RuntimeError(f"Google Scholar returned HTTP {error.code}.") from error
    except URLError as error:
        raise RuntimeError(f"Could not reach Google Scholar: {error.reason}") from error

    block_markers = (
        "Our systems have detected unusual traffic",
        "recaptcha",
        "We're sorry",
    )
    if any(marker.lower() in html.lower() for marker in block_markers):
        raise RuntimeError("Google Scholar blocked this request.")

    return html


def meta_content(soup: BeautifulSoup, selector: str) -> str:
    element = soup.select_one(selector)
    if not element:
        return ""
    return clean_text(element.get("content"))


def extract_stats(soup: BeautifulSoup) -> dict[str, int]:
    stats: dict[str, int] = {}
    key_map = {
        "Citations": ("citedby", "citedby5y"),
        "h-index": ("hindex", "hindex5y"),
        "i10-index": ("i10index", "i10index5y"),
    }

    for row in soup.select("#gsc_rsb_st tbody tr"):
        cells = [clean_text(cell.get_text(" ", strip=True)) for cell in row.select("td")]
        if len(cells) < 2 or cells[0] not in key_map:
            continue

        current_key, recent_key = key_map[cells[0]]
        current_value = parse_int(cells[1])
        recent_value = parse_int(cells[2]) if len(cells) > 2 else None

        if current_value is not None:
            stats[current_key] = current_value
        if recent_value is not None:
            stats[recent_key] = recent_value

    description = meta_content(soup, 'meta[name="description"]')
    if "citedby" not in stats:
        citedby_match = re.search(r"Cited by\s+([\d,]+)", description, re.IGNORECASE)
        if citedby_match:
            stats["citedby"] = int(citedby_match.group(1).replace(",", ""))

    return stats


def extract_cites_per_year(soup: BeautifulSoup) -> dict[str, int]:
    years = [clean_text(node.get_text(" ", strip=True)) for node in soup.select(".gsc_g_t")]
    counts = [parse_int(node.get_text(" ", strip=True)) for node in soup.select(".gsc_g_al")]
    return {
        year: count
        for year, count in zip(years, counts)
        if year and count is not None
    }


def extract_publications(soup: BeautifulSoup) -> dict[str, dict[str, Any]]:
    publications: dict[str, dict[str, Any]] = {}

    for index, row in enumerate(soup.select("tr.gsc_a_tr"), start=1):
        title_link = row.select_one("a.gsc_a_at")
        if not title_link:
            continue

        href = title_link.get("href", "")
        query = parse_qs(urlparse(href).query)
        author_pub_id = query.get("citation_for_view", [f"publication-{index}"])[0]
        gray_rows = row.select(".gs_gray")
        citedby_link = row.select_one(".gsc_a_c a")
        cites_id = []
        if citedby_link:
            cites_id = parse_qs(urlparse(citedby_link.get("href", "")).query).get("cites", [])

        publication: dict[str, Any] = {
            "container_type": "Publication",
            "source": "AUTHOR_PUBLICATION_ENTRY",
            "bib": {
                "title": clean_text(title_link.get_text(" ", strip=True)),
            },
            "filled": False,
            "author_pub_id": author_pub_id,
            "num_citations": parse_int(
                citedby_link.get_text(" ", strip=True) if citedby_link else ""
            ) or 0,
        }

        if gray_rows:
            publication["bib"]["author"] = clean_text(gray_rows[0].get_text(" ", strip=True))
        if len(gray_rows) > 1:
            publication["bib"]["citation"] = clean_text(gray_rows[1].get_text(" ", strip=True))

        year_node = row.select_one(".gsc_a_y .gsc_a_h")
        year = clean_text(year_node.get_text(" ", strip=True)) if year_node else ""
        if year:
            publication["bib"]["pub_year"] = year

        if citedby_link and citedby_link.get("href"):
            publication["citedby_url"] = urljoin("https://scholar.google.com", citedby_link["href"])
        if cites_id:
            publication["cites_id"] = cites_id

        publications[author_pub_id] = publication

    return publications


def build_author_payload(scholar_id: str, html: str) -> dict[str, Any]:
    soup = BeautifulSoup(html, "html.parser")
    stats = extract_stats(soup)
    publications = extract_publications(soup)

    if not stats.get("citedby") and not publications:
        raise RuntimeError("Google Scholar profile page did not contain citation data.")

    name_node = soup.select_one("#gsc_prf_in")
    name = (
        clean_text(name_node.get_text(" ", strip=True))
        if name_node
        else meta_content(soup, 'meta[property="og:title"]')
    )
    profile_lines = [
        clean_text(node.get_text(" ", strip=True))
        for node in soup.select("#gsc_prf_i .gsc_prf_il")
    ]
    url_picture = ""
    picture = soup.select_one("#gsc_prf_pup-img")
    if picture and picture.get("src"):
        url_picture = urljoin("https://scholar.google.com", picture["src"])

    author: dict[str, Any] = {
        "container_type": "Author",
        "filled": ["basics", "publications", "indices", "counts"],
        "scholar_id": scholar_id,
        "source": "AUTHOR_PROFILE_PAGE",
        "name": name,
        "url_picture": url_picture,
        "interests": [
            clean_text(node.get_text(" ", strip=True))
            for node in soup.select("#gsc_prf_int a")
        ],
        "publications": publications,
        "cites_per_year": extract_cites_per_year(soup),
        "updated": datetime.now(timezone.utc).isoformat(),
        "fetch_status": "fresh",
    }

    if profile_lines:
        author["affiliation"] = profile_lines[0]

    for line in profile_lines[1:]:
        if "verified email" in line.lower():
            match = re.search(r"verified email at\s+([\w.-]+)", line, re.IGNORECASE)
            if match:
                author["email_domain"] = f"@{match.group(1)}"
        elif line.startswith("http://") or line.startswith("https://"):
            author["homepage"] = line

    author.update(stats)
    return author


def load_fallback() -> dict[str, Any] | None:
    fallback_path = RESULTS_DIR / "gs_data.json"
    if not fallback_path.exists():
        return None

    try:
        return json.loads(fallback_path.read_text())
    except json.JSONDecodeError:
        return None


def fallback_payload(scholar_id: str, error: Exception) -> dict[str, Any]:
    fallback = load_fallback()
    if fallback is None:
        raise RuntimeError("No previous Scholar data is available for fallback.") from error

    fallback["fetch_status"] = "stale_fallback"
    fallback["last_fetch_error"] = str(error)
    fallback["last_fetch_attempt"] = datetime.now(timezone.utc).isoformat()
    fallback.setdefault("scholar_id", scholar_id)
    return fallback


def write_outputs(author: dict[str, Any]) -> None:
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    (RESULTS_DIR / "gs_data.json").write_text(
        json.dumps(author, ensure_ascii=False),
        encoding="utf-8",
    )

    shieldio_data = {
        "schemaVersion": 1,
        "label": "citations",
        "message": str(author.get("citedby", "unavailable")),
    }
    (RESULTS_DIR / "gs_data_shieldsio.json").write_text(
        json.dumps(shieldio_data, ensure_ascii=False),
        encoding="utf-8",
    )


def main() -> int:
    scholar_id = read_scholar_id()

    try:
        author = build_author_payload(scholar_id, fetch_profile_html(scholar_id))
    except Exception as error:
        print(f"Fresh Google Scholar fetch failed: {error}", file=sys.stderr)
        author = fallback_payload(scholar_id, error)
        print("Using previous citation data from google-scholar-stats.", file=sys.stderr)

    write_outputs(author)
    print(json.dumps(author, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
