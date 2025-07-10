import click
from get_papers.fetcher import fetch_pubmed_ids, fetch_pubmed_details
from get_papers.filters import extract_company_affiliations
from get_papers.writer import write_to_csv

@click.command()
@click.argument('query')
@click.option('-f', '--file', 'file_', help='CSV output filename')
@click.option('-d', '--debug', is_flag=True, help='Enable debug logging')
def main(query: str, file_: str, debug: bool):
    ids = fetch_pubmed_ids(query, debug)
    if not ids:
        click.echo("🔍 No papers found for query.", err=True)
        return
    xml = fetch_pubmed_details(ids, debug)
    rows = extract_company_affiliations(xml)
    if not rows:
        click.echo("⚠️ No non-academic authors found.")
        return
    write_to_csv(rows, file_)
    click.echo(f"✅ Output saved to {file_}" if file_ else "✅ Done (printed above)")

if __name__ == '__main__':
    main()