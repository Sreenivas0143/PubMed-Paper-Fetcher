import requests
from typing import List
import logging

def fetch_pubmed_ids(query: str, debug: bool = False) -> List[str]:
    if debug:
        logging.basicConfig(level=logging.DEBUG)
    url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    params = {
        "db": "pubmed",
        "term": query,
        "retmode": "json",
        "retmax": "100"
    }
    r = requests.get(url, params=params)
    r.raise_for_status()
    data = r.json()
    if debug:
        logging.debug("ESearch result: %s", data)
    return data["esearchresult"].get("idlist", [])

def fetch_pubmed_details(ids: List[str], debug: bool = False) -> str:
    url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
    params = {
        "db": "pubmed",
        "id": ",".join(ids),
        "retmode": "xml"
    }
    r = requests.get(url, params=params)
    r.raise_for_status()
    if debug:
        logging.debug("EFetch XML starts with: %s", r.text[:500])
    return r.text