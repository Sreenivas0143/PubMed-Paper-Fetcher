# 📄 PubMed-Paper-Fetcher

**CLI tool to fetch PubMed papers with authors affiliated to pharma/biotech companies.**

**PubMed Paper Fetcher** is a Python-based command-line tool that allows users to search for research papers from **PubMed** using any query. It intelligently identifies papers with at least one author affiliated with **pharmaceutical or biotech companies**, using heuristics like keywords in affiliations or email domains.

It extracts and outputs the following details:

- **PubMed ID**
- **Title**
- **Publication Date**
- **Non-academic Author(s)**
- **Company Affiliation(s)**
- **Corresponding Author Email**

The tool supports full PubMed query syntax, outputs results as a **CSV file** or to the **console**, and is designed with clean architecture using **typed Python**, **Poetry**, and **Click** for a smooth CLI experience.

This project is ideal for **HR recruiters**, **researchers**, and **data analysts** seeking structured insights into industry-linked biomedical publications.

---

## 🚀 Features

- Uses **PubMed ESearch** + **EFetch** APIs
- Filters **non-academic authors** via keyword-based heuristics
- Outputs **CSV** (to file or console)
- Built with **Poetry**, **typed Python**, and a polished CLI

---

## 🛠️ Setup

```bash
git clone https://github.com/Sreenivas0143/get-papers.git
cd get-papers
poetry install

## Features

- Uses PubMed ESearch + EFetch
- Filters non-academic authors (via keyword heuristics)
- Outputs CSV (file or console)
- Built with Poetry, typed Python, and good CLI UX

## Setup

```bash
git clone https://github.com/Sreenivas0143/PubMed-Paper-Fetcher.git
cd PubMed-Paper-Fetcher
poetry install

## Usage
Replace the query string with any valid PubMed search term. Below are example commands:

## Fetch and print to console:

poetry run get-papers-list "cancer immunotherapy"

## Fetch and save to CSV with debug:

poetry run get-papers-list "COVID-19 vaccine" -f covid.csv -d

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
