import csv
from typing import List, Tuple, Optional

def write_to_csv(
    rows: List[Tuple[str, str, str, str, str, str]],
    filename: Optional[str]
) -> None:
    out = open(filename, 'w', newline='', encoding='utf-8') if filename else None
    writer = csv.writer(out or __import__('sys').stdout)
    writer.writerow([
        'PubmedID', 'Title', 'Publication Date',
        'Non-academic Author(s)', 'Company Affiliation(s)',
        'Corresponding Author Email'
    ])
    for r in rows:
        writer.writerow(r)
    if out:
        out.close()