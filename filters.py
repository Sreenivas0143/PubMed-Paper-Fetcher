from typing import List, Tuple
import re
import xml.etree.ElementTree as ET

def is_non_academic(aff: str) -> bool:
    keywords = ['university', 'college', 'school', 'institute', 'hospital', 'department']
    aff_low = aff.lower()
    return not any(k in aff_low for k in keywords)

def extract_company_affiliations(xml_data: str) -> List[Tuple[str, str, str, str, str, str]]:
    root = ET.fromstring(xml_data)
    results = []
    for art in root.findall('.//PubmedArticle'):
        pmid = art.findtext('.//PMID') or ''
        title = art.findtext('.//ArticleTitle') or ''
        year = art.findtext('.//PubDate/Year') or ''
        authors = art.findall('.//Author')
        for author in authors:
            aff = author.findtext('.//AffiliationInfo/Affiliation')
            if aff and is_non_academic(aff):
                lname = author.findtext('LastName') or ''
                fname = author.findtext('ForeName') or ''
                full_name = f"{fname} {lname}".strip()
                email_match = re.search(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", aff)
                email = email_match.group(0) if email_match else ''
                results.append((pmid, title, year, full_name, aff, email))
    return results