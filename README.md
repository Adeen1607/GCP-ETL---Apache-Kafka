# News ETL with Kafka and Hive

Original GCP Kafka Project.docx coursework report and embedded screenshots.


## Rebuild the reading edition

```bash
python -m pip install -r requirements-research.txt
python scripts/build_research_site.py
```

This renders saved notebook outputs without rerunning model training or external APIs. To refresh findings, run the analysis commands above first, update `reports/research-findings.md`, and rebuild.

<!-- research-edition:start -->
## Research edition

[Research report and final visual results](research/report.md) · [Browser-ready notebook catalogue](research/notebooks.html)

The historical report records **16 articles** in the demonstrated Hive table. This verifies the scope of the documented example, not throughput, latency, fault tolerance or production scale. An exposed credential was removed from the current document; old Git history and provider-side validity are separate concerns.


The `research/` folder contains a professional static reading edition. The Pages workflow deploys it after GitHub Pages is enabled with **GitHub Actions** as the publishing source. Intended URL: `https://adeen1607.github.io/GCP-ETL---Apache-Kafka/`. Deployment status must be checked in Actions before treating that address as live.

<!-- research-edition:end -->
