# ethanscuter.github.io

Personal academic homepage of **Xintong Wang (王鑫同)** — built with Jekyll on top of the
[AcadHomepage](https://github.com/RayeRen/acad-homepage.github.io) template by Yi Ren.

## Local development

```bash
bundle install --path vendor/bundle
bundle exec jekyll serve
```

The site will be available at <http://127.0.0.1:4000/>.

## Editing

Most content lives in `_pages/about.md` (the homepage) and `_data/navigation.yml` (the top
menu). Author information and social links can be configured in `_config.yml`.

Paper teaser images live in `images/`; full publication PDFs in `pdf/`.

## Google Scholar citation badge

The citation count badge in the intro paragraph is fed by `gs_data_shieldsio.json` on the
`google-scholar-stats` branch (auto-refreshed daily by
`.github/workflows/google_scholar_crawler.yaml`).

To enable / refresh it on the live site, add a repository secret named
`GOOGLE_SCHOLAR_ID = xYfO9VEAAAAJ` under **Settings → Secrets and variables → Actions**.
The action will then push the latest snapshot to the `google-scholar-stats` branch every
night at 08:00 UTC and on every page build.

You can also regenerate the JSON locally:

```bash
cd google_scholar_crawler
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
GOOGLE_SCHOLAR_ID=xYfO9VEAAAAJ python3 main.py
```

## Credits

Template: [AcadHomepage](https://github.com/RayeRen/acad-homepage.github.io) (MIT License).
