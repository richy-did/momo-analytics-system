# MoMo Analytics System

A solo-team project for processing MoMo SMS XML data, normalizing transactions, storing them in SQLite, and presenting KPI summaries in a lightweight dashboard.

## Project overview
This repository contains a starter full-stack analytics pipeline for the assignment. It follows an ETL workflow:

1. Parse raw MoMo SMS XML data.
2. Clean and normalize transaction fields such as phone numbers, amounts, and dates.
3. Categorize each transaction by type.
4. Load the cleaned records into SQLite.
5. Export aggregated data for the frontend dashboard.
6. Render key visuals in a static web dashboard.

## Team and assignment context
- Team name: MoMo Analytics System
- Team members: Solo developer / Munezero jean pierre
- Repository purpose: Enterprise-style data processing and analytics prototype
- This is an individual submission completed as a solo project, following the instructor's direction for joining the assignment late.

## Architecture diagram
- Diagram file: [docs/architecture-diagram.svg](docs/architecture-diagram.svg)
- Mermaid source: [docs/architecture-diagram.md](docs/architecture-diagram.md)

## Scrum board
- Project board: https://github.com/richy-did/momo-analytics-system/projects/1
- Planning notes: [Trello Board](https://trello.com/invite/b/6aa6bf968f97117846531f5c/ATTI15e19514e98934e86037c961b89eb270BE2C38CF/momo-analytics-system)

> Since this is a solo project, the work is organized as a single-person Agile board with the required To Do, In Progress, and Done columns.

## Local setup

```bash
python -m venv .venv
. .venv/bin/activate  # Windows: .venv\Scripts\activate
python -m pip install -r requirements.txt
python etl/run.py --xml data/raw/momo.xml
python -m http.server 8000
```

Then open http://localhost:8000 in a browser.

## Project structure

```text
.
├── README.md
├── .env.example
├── requirements.txt
├── index.html
├── web/
│   ├── styles.css
│   ├── chart_handler.js
│   └── assets/
├── data/
│   ├── raw/
│   │   └── momo.xml
│   ├── processed/
│   │   └── dashboard.json
│   ├── db.sqlite3
│   └── logs/
│       ├── etl.log
│       └── dead_letter/
├── etl/
│   ├── __init__.py
│   ├── config.py
│   ├── parse_xml.py
│   ├── clean_normalize.py
│   ├── categorize.py
│   ├── load_db.py
│   └── run.py
├── api/
│   ├── __init__.py
│   ├── app.py
│   ├── db.py
│   └── schemas.py
├── scripts/
│   ├── run_etl.sh
│   ├── export_json.sh
│   └── serve_frontend.sh
├── docs/
│   ├── architecture-diagram.md
│   ├── architecture-diagram.svg
│   └── scrum-board.md
├── tests/
│   ├── test_parse_xml.py
│   ├── test_clean_normalize.py
│   └── test_categorize.py
├── .gitignore
└── .env.example
```

## Deliverables checklist
- [x] GitHub repository documentation prepared
- [x] Architecture diagram included in the repo
- [x] Scrum board notes included in the repo
- [x] ETL pipeline starter implemented
- [x] Frontend dashboard starter implemented
- [x] SQLite storage starter implemented
- [x] Test scaffold created

## Notes
This repository is intentionally set up as a solid starter project for the assignment and can be pushed to a GitHub remote once the repository is created.
