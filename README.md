# 📄 get-papers

CLI tool to fetch PubMed papers with authors affiliated to pharma/biotech companies.

## Features

- Uses PubMed ESearch + EFetch
- Filters non-academic authors (via keyword heuristics)
- Outputs CSV (file or console)
- Built with Poetry, typed Python, and good CLI UX

## Setup

```bash
git clone https://github.com/Sreenivas0143/get-papers.git
cd get-papers
poetry install
```

## Usage

Fetch and print:

```bash
poetry run get-papers-list "cancer immunotherapy"
```

Fetch and save CSV:

```bash
poetry run get-papers-list "COVID-19 vaccine" -f covid.csv -d
```

## Code Structure

- `fetcher.py`: PubMed API wrappers
- `filters.py`: XML parsing + heuristics
- `writer.py`: CSV output
- `cli.py`: Entry point (Click)

## Dependencies & Tools

- [requests] for HTTP calls
- [click] for CLI
- [poetry] for dependency management
- [mypy] for type checking