---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from:
  - /about/
  - /about.html
---

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}

<span class='anchor' id='about-me'></span>

I am currently a **Senior Agentic AI Applied Scientist** at the CBU Technology Department of [Taobao & Tmall Group (Alibaba)](https://www.alibabagroup.com/) in Hangzhou, China, where I serve as **Tech Lead of the Multimodal Team**, driving trillion-parameter–scale RL models and architecting a multimodal agent collaboration framework for coordinated perception, reasoning, and action. In parallel, I am a **Habilitation-track Researcher** and **Ph.D. Co-Supervisor** at the [Hub of Computing & Data Science](https://www.hcds.uni-hamburg.de/), [University of Hamburg](https://www.uni-hamburg.de/en.html), working with Prof. [Chris Biemann](https://www.inf.uni-hamburg.de/en/inst/ab/lt/people/chris-biemann.html).

I received my Ph.D. *summa cum laude* from the [University of Hamburg](https://www.uni-hamburg.de/en.html) in May 2026, advised by Prof. [Chris Biemann](https://www.inf.uni-hamburg.de/en/inst/ab/lt/people/chris-biemann.html). My doctoral thesis is "*Bridging Vision, Language, and Gaze for Trustworthy Foundation Models*". Previously, I obtained my M.Eng. (2019) and B.Eng. (2016) degrees from the School of Computer Science and Engineering, [South China University of Technology](https://www.scut.edu.cn/en/).

My research focuses on **large language models and agentic systems**, with an emphasis on **training and alignment, evaluation and interpretability, and multilingual and multimodal learning** for real-world applications. I have published 20+ papers in top international AI venues such as ACL, EMNLP, NAACL, COLING and ECAI <a href='https://scholar.google.com/citations?user=xYfO9VEAAAAJ&hl=en'><img src="https://img.shields.io/endpoint?url={{ url | url_encode }}&logo=Google%20Scholar&labelColor=f6f6f6&color=9cf&style=flat&label=citations"></a>.

💌 *hanfeng.wxt@alibaba-inc.com* / *xintong.wang@uni-hamburg.de* / *m.e.xintong@gmail.com*

🤝 **Opening:** We are hiring [full-time positions & interns](https://liamding.cc/hiring.html) at Alibaba, and student assistants at the University of Hamburg. Self-motivated students with experience in LLMs, LVLMs, and Agents are welcome to reach out. Please feel free to drop me an email — I am always open to collaborations.


# 🔥 News
- *2026.06*: &nbsp;💼 I joined the CBU Technology Department, Taobao & Tmall Group (Alibaba) as a Senior Agentic AI Applied Scientist in Hangzhou.
- *2026.05*: &nbsp;🎓 I successfully defended my Ph.D. dissertation at the University of Hamburg (*summa cum laude*).
- *2025.08*: &nbsp;🎉 One paper accepted to **EMNLP 2025 (Main, Top 15%)**!
- *2025.05*: &nbsp;🎉 Three papers accepted to **ACL 2025**!
- *2024.12*: &nbsp;😊 Serving as an **Area Chair** for ACL ARR / NAACL 2025!
- *2024.11*: &nbsp;🎉 One paper accepted to **COLING 2025 (Oral)**!
- *2024.05*: &nbsp;🎉 One paper accepted to **ACL 2024 (Findings)**!
- *2024.03*: &nbsp;🎉 One paper accepted to **LREC-COLING NeusymBridge 2024**!
- *2023.08*: &nbsp;🛠 Co-organizer of CLEF-2024 SemEval Task: Multilingual Text Detoxification.
- *2023.07*: &nbsp;🎉 One paper accepted to **ECAI 2023**!
- *2023.06*: &nbsp;🎤 Invited talk at the University of Wuppertal.
- *2022.12*: &nbsp;✈️ Visiting Researcher at the Institute of Psychology, Chinese Academy of Sciences.
- *2022.05*: &nbsp;🎉 One paper accepted to **LREC 2022**!
- *2021.04*: &nbsp;🎓 Started as a Ph.D. Candidate at the University of Hamburg.


# 📝 Publications

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">EMNLP 2025</div><img src='images/paper_emnlp2025.png' alt="EMNLP 2025" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Chinese Toxic Language Mitigation via Sentiment Polarity Consistent Rewrites](pdf/EMNLP2025Wang.pdf) <a href="https://github.com/PostMindLab/ToxiRewriteCN" title="Code on GitHub"><i class="fab fa-github"></i></a> <a href="https://huggingface.co/datasets/shanewang/ToxiRewriteCN" title="Dataset on Hugging Face">🤗</a>

**Xintong Wang**, Yixiao Liu, Jingheng Pan, Liang Ding, Longyue Wang, Chris Biemann

*The 2025 Conference on Empirical Methods in Natural Language Processing* (**EMNLP 2025**, Main, Top 15%)

- We present **TOXIREWRITECN**, the first Chinese detoxification dataset that explicitly preserves sentiment polarity, with 1,556 carefully annotated triplets covering five real-world scenarios.
- Comprehensive evaluation across 17 commercial and open-source LLMs reveals key limitations in sentiment-aware detoxification.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ACL 2025</div><img src='images/paper_acl2025.png' alt="ACL 2025" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[CogSteer: Cognition-Inspired Selective Layer Intervention for Efficiently Steering Large Language Models](https://arxiv.org/abs/2410.17714) <a href="https://github.com/PostMindLab/cogsteer" title="Code on GitHub"><i class="fab fa-github"></i></a>

**Xintong Wang**, Jingheng Pan, Liang Ding, Longyue Wang, Longqin Jiang, Xingshan Li, Chris Biemann

*Findings of the Association for Computational Linguistics* (**ACL 2025**)

- We leverage eye-movement measures to analyze the layer-wise behavior of LLMs and propose a heuristic strategy for selecting the optimal steering layer for semantic intervention.
- Our framework requires only 1/N of LLM parameters and achieves +1.85% gain in toxification and +13.45% in detoxification compared to last-layer intervention.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ACL 2024</div><img src='images/paper_acl2024.png' alt="ACL 2024" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Mitigating Hallucinations in Large Vision-Language Models with Instruction Contrastive Decoding](https://aclanthology.org/2024.findings-acl.937.pdf) <a href="https://github.com/PostMindLab/ICD" title="Code on GitHub"><i class="fab fa-github"></i></a>

**Xintong Wang**, Jingheng Pan, Liang Ding, Chris Biemann

*Findings of the Association for Computational Linguistics* (**ACL 2024**)

- A training-free Instruction Contrastive Decoding (ICD) method that contrasts standard and disturbance-instruction distributions to suppress hallucinations in LVLMs.
- Significantly mitigates both object-level and attribute-level hallucinations on POPE, MME, and LLaVA-Bench, while improving general perception and recognition.
</div>
</div>

### Full Publication List

(\* denotes equal contribution; <sup>✉️</sup> denotes corresponding author)

- `Preprint 2026` [A Multimodal Dataset for Visually Grounded Ambiguity in Machine Translation](https://arxiv.org/pdf/2605.02035v1) <a href="https://huggingface.co/datasets/p1k0/visually-dependent-ambiguity" title="Dataset on Hugging Face">🤗</a>, Jingheng Pan, **Xintong Wang**<sup>✉️</sup>, Longyue Wang, Liang Ding, Weihua Luo, Chris Biemann. *Under Review (ACL ARR).*
- `Preprint 2025` [Perception, Reason, Think, and Plan: A Survey on Large Multimodal Reasoning Models](https://arxiv.org/abs/2505.04921), Yunxin Li, Zhenyu Liu, Zitao Li, Xuanyu Zhang, Zhenran Xu, Xinyu Chen, Haoyuan Shi, Shenyuan Jiang, **Xintong Wang**, Jifang Wang, Shouzheng Huang, Xinping Zhao, Borui Jiang, Lanqing Hong, Longyue Wang, Zhuotao Tian, Baoxing Huai, Wenhan Luo, Zheng Zhang, Baotian Hu, Min Zhang. *Under Review at ACM Computing Surveys.*
- `Preprint 2025` [Rethinking Multilingual Vision-Language Translation: Dataset, Evaluation, and Adaptation](https://arxiv.org/abs/2510.01918), **Xintong Wang**, Jingheng Pan, Yixiao Liu, Xiaohu Zhao, Chenyang Lyu, Minghao Wu, Chris Biemann, Longyue Wang, Linlong Xu, Weihua Luo, Kaifu Zhang. *Under Review (ACL ARR).*
- `Preprint 2025` [The Bitter Lesson Learned from 2,000+ Multilingual Benchmarks](https://arxiv.org/abs/2504.15521), Minghao Wu, Weixuan Wang, Sinuo Liu, Huifeng Yin, **Xintong Wang**, Yu Zhao, Chenyang Lyu, Longyue Wang, Weihua Luo, Kaifu Zhang. *Under Review (ACL ARR).*
- `EMNLP 2025` [Chinese Toxic Language Mitigation via Sentiment Polarity Consistent Rewrites](pdf/EMNLP2025Wang.pdf) <a href="https://github.com/PostMindLab/ToxiRewriteCN" title="Code on GitHub"><i class="fab fa-github"></i></a> <a href="https://huggingface.co/datasets/shanewang/ToxiRewriteCN" title="Dataset on Hugging Face">🤗</a>, **Xintong Wang**, Yixiao Liu, Jingheng Pan, Liang Ding, Longyue Wang, Chris Biemann. *Main Conference, Top 15%.*
- `ACL 2025` [CogSteer: Cognition-Inspired Selective Layer Intervention for Efficiently Steering Large Language Models](https://arxiv.org/abs/2410.17714) <a href="https://github.com/PostMindLab/cogsteer" title="Code on GitHub"><i class="fab fa-github"></i></a>, **Xintong Wang**, Jingheng Pan, Liang Ding, Longyue Wang, Longqin Jiang, Xingshan Li, Chris Biemann. *Findings.*
- `ACL 2025` [Metagent-P: A Neuro-Symbolic Planning Agent with Metacognition for Open Worlds](https://aclanthology.org/2025.findings-acl.1234/), Yanfang Zhou, Yuntao Liu, Xiaodong Li, Yongqiang Zhao, **Xintong Wang**, Qingyu Wu, Jinlong Tian, Zhenyu Li, Xinhai Xu. *Findings.*
- `ACL 2025` [M2PA: A Multi-Memory Planning Agent for Open Worlds Inspired by Cognitive Theory](https://aclanthology.org/2025.findings-acl.1235/), Yanfang Zhou, Xiaodong Li, Yuntao Liu, Yongqiang Zhao, **Xintong Wang**, Zhenyu Li, Jinlong Tian, Xinhai Xu. *Findings.*
- `COLING 2025` [Multilingual and Explainable Text Detoxification with Parallel Data](pdf/COLING2025.pdf), Daryna Dementieva, Daniil Moskovskiy, Nikolai Babakov, Abinew Ali Ayele, Naquee Rizwan, Florian Schneider, **Xintong Wang**, Seid Muhie Yimam, Dmitry Ustalov, Elisei Stakovskii, Alisa Smirnova, Ashraf Elnagar, Animesh Mukherjee, Alexander Panchenko. *Oral.*
- `ACL 2024` [Mitigating Hallucinations in Large Vision-Language Models with Instruction Contrastive Decoding](https://aclanthology.org/2024.findings-acl.937.pdf) <a href="https://github.com/PostMindLab/ICD" title="Code on GitHub"><i class="fab fa-github"></i></a>, **Xintong Wang**, Jingheng Pan, Liang Ding, Chris Biemann. *Findings.*
- `CLEF 2024` [Overview of PAN 2024: Multi-Author Writing Style Analysis, Multilingual Text Detoxification, Oppositional Thinking Analysis, and Generative AI Authorship Verification](pdf/CLEF2024.pdf), Abinew Ali Ayele, Nikolay Babakov, Janek Bevendorff, Xavier Bonet Casals, Berta Chulvi, Daryna Dementieva, ..., **Xintong Wang**, Matti Wiegmann, Seid Muhie Yimam, Eva Zangerle.
- `CLEF 2024` [Overview of the Multilingual Text Detoxification Task at PAN 2024](https://ceur-ws.org/Vol-3740/paper-223.pdf), Daryna Dementieva, Daniil Moskovskiy, Nikolai Babakov, Abinew Ali Ayele, Naquee Rizwan, Florian Schneider, **Xintong Wang**, Seid Muhie Yimam, et al.
- `LREC-COLING 2024` [Probing Large Language Models from a Human Behavioral Perspective](pdf/NeusymBridge2024Wang.pdf), **Xintong Wang**, Xiaoyu Li, Xingshan Li, Chris Biemann. *NeusymBridge Workshop.*
- `ECAI 2023` [Using Self-Supervised Dual Constraint Contrastive Learning for Cross-modal Retrieval](pdf/ECAI2023Wang.pdf), **Xintong Wang**, Xiaoyu Li, Liang Ding, Sanyuan Zhao, Chris Biemann.
- `AACL-IJCNLP SRW 2022` [Language over Labels: Contrastive Language Supervision Exceeds Purely Label-Supervised Classification Performance on Chest X-Rays](https://aclanthology.org/2022.aacl-srw.11/), Anton Orell Wiehe, Florian Schneider, Sebastian Blank, **Xintong Wang**, Hans-Peter Zorn, Chris Biemann.
- `LREC 2022` [MOTIF: Contextualized Images for Complex Words to Improve Human Reading](pdf/LREC2022.Wang.pdf) <a href="https://huggingface.co/datasets/shanewang/MOTIF" title="Dataset on Hugging Face">🤗</a>, **Xintong Wang\***, Florian Schneider\*, Özge Alaçam, Prateek Chaudhury, Chris Biemann.
- `NAACL SRW 2021` [Towards Multi-Modal Text-Image Retrieval to Improve Human Reading](pdf/NAACL@SRW2021.Schneider.pdf), Florian Schneider, Özge Alaçam, **Xintong Wang**, Chris Biemann.
- `Information Sciences 2020` [Plausibility-promoting Generative Adversarial Network for Abstractive Text Summarization with Multi-task Constraint](https://www.sciencedirect.com/science/article/pii/S0020025520301328), Min Yang, **Xintong Wang**, Yao Lu, Jianming Lv, Ying Shen, Chengming Li. *JCR-Q1.*


# 🧑‍🏫 Teaching
- *Winter 2025 & 2026*, **Lecturer**, *Exercises Natural Language Processing and the Web* (Master), University of Hamburg.
- *Summer 2025 & 2026*, **Lecturer**, *Exercises Statistical Methods of Language Technology* (Master), University of Hamburg.
- *Winter 2024*, **Teaching Assistant**, *Introduction to Python for Research* (Bachelor / Master / PhD), Max Planck Institute.
- *Winter 2024*, **Co-Instructor**, *Deep Learning for Natural Language Processing* (Bachelor), University of Hamburg.
- *Summer 2022 & 2023*, **Project Mentor**, *Web Interfaces for Language Processing Systems* (Master Project), University of Hamburg.
- *Winter 2020*, **Co-Lecturer**, *Natural Language Processing and the Web* (Master), University of Hamburg.


# 🎓 Supervision

**Co-Supervised Doctoral Students**
- **Jingheng Pan** (Ph.D. Candidate, Universität Hamburg, 2025 – present) — *LVLM Post-Training, Reasoning*.
- **Yixiao Liu** (Ph.D. Candidate, Universität Hamburg, 2026 – present) — *LLM Post-Training, Interpretability, Cognitive Analysis*.

**Supervised Master Students**
- **Longqin Jiang** (M.Sc. Student, Universität Hamburg, 2025 – present) — *In-Image Text Understanding, Vision-Language Models*.
- **Jingfan Xin** (M.Sc. Student, Universität Hamburg, 2025 – present) — *Large Reasoning Models*.

**Interns**
- **Duo Li** (Ph.D. Candidate, Nanyang Technological University, 2026 Summer) — *Multimodal Agents*.
- **Qingyu Lu** (Ph.D. Candidate, Southeast University, 2026 Summer) — *LLM Post-Training, RL*.
- **Yuchen Wu** (Ph.D. Candidate, Shanghai Jiao Tong University, 2026 Summer) — *Agent Memory*.
- **Haonan Qi** (M.Sc. Student, Shanghai Jiao Tong University, 2026 Summer) — *Vision-Language Reasoning*.
- **Yongqi Zhang** (M.Sc. Student, Southeast University, 2026 Summer) — *Multimodal LLMs*.

**Previous Students**
- **Xiaoyu Li** (M.Sc., TU Berlin & Beijing Institute of Technology, 2024) — *Foundation Models, Cross-Modal Representation Learning*.
- **Fabian Meyer** (M.Sc., Universität Hamburg, 2023) — *Out-of-Distribution Detection, Robustness*.
- **Anton Orell Wiehe** (M.Sc., Universität Hamburg, 2022) — *Domain Adaptation, Multi-Modal Foundation Models*.
- **Matthew Ng Cher-Wai** (M.Sc., Universität Hamburg, 2022) — *Multi-Modal Generation, Transformers*.
- **Ankit Srivastava** (M.Sc., Universität Hamburg, 2022) — *Lexical Simplification, Educational NLP*.
- **Florian Schneider** (M.Sc., Universität Hamburg, 2021) — *Self-Supervised Multi-Modal Retrieval*. *GSCL Best Master's Thesis Award 2023.*
- **Prateek Chaudhury** (B.Sc., IIT Delhi, 2021) — *Educational NLP, Reading Comprehension*.


# 🎖 Honors and Awards
- *2025*, Alibaba Group AliStar Program — *Offer declined*.
- *2025*, Alibaba International AliStar Program — *Offer declined*.
- *2025*, Huawei Genius Youth Program — *Offer declined*.
- *2025*, Ant Group AntStar Plan A Program — *Offer declined*.
- *2023*, ECAI 2023 Travel Grant Award, 26th European Conference on Artificial Intelligence.


# 💬 Invited Talks
- *2025.03*, *Multimodal Representation Learning: Understanding and Leveraging*. Host: Prof. Jianming Lv, South China University of Technology.
- *2024.08*, *Towards Truthfulness, Safeness, and Explainable Advanced Foundation Models*. Host: Prof. Xingshan Li, Institute of Psychology, Chinese Academy of Sciences.
- *2024.07*, *Mitigating Hallucinations in Large Vision-Language Models (LVLMs)*. Online Talk.
- *2024.05*, *Probing Large Language Models from a Human Behavioral Perspective*. Host: Dr. Tiansi Dong, NeusymBridge @ LREC-COLING 2024.
- *2023.06*, [*Probing Large Language Models (LLMs) for Predicting Human Behavioral Data*](pdf/Wuppertal_Talk_2023.pdf). Hosts: Prof. Markus Hofmann & Prof. Ralph Radach, Universität Wuppertal.


# 🛠 Academic Services

**Funding Reviewer**
- Vienna Science and Technology Fund — *Vienna Research Groups for Young Investigators* (2025).

**Workshop & Shared Task Organization**
- POLAR @ SemEval 2026 — *Attitude Polarization Detection in Multilingual Text*.
- CLEF 2025 SemEval Task — *Multilingual Text Detoxification*.
- CLEF 2024 SemEval Task — *Multilingual Text Detoxification*.

**Area Chair**
- ACL Rolling Review (ARR) — *Multimodal Learning*, 2024 – 2025.

**Session Chair**
- ECAI 2023 — *Speech and Natural Language Processing*.

**Conference Reviewer**
- ACL, EMNLP, NAACL, EACL, COLING, LREC-COLING, IJCNLP-AACL, AAAI, IJCAI, NeurIPS, AISTATS, CVPR, ECCV, ACM MM, ECAI — 2019 – present.
- IJCAI 2021 — Senior Program Committee.

**Journal Reviewer**
- ACM TALLIP (2020 – 2021); IEEE Access (2020 – 2021).


# 🐈 Misc.
I have a cat called *Minus* — his name is the German word for *subtraction*, with my hope that he can live life on easy mode.
