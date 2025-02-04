from bs4 import BeautifulSoup

def main():
    html_file = "algorai.html"
    with open(html_file, "r", encoding="utf-8") as f:
        html_content = f.read()

    soup = BeautifulSoup(html_content, "html.parser")

    assignment_table = find_table(soup, "Atsiskaitymas")
    if not assignment_table:
        return

    rows = get_relevant_rows(assignment_table)

    for row in rows:
        cells = row.find_all("td")
        print(cells[0])

def find_table(soup: BeautifulSoup, table_name):
    table_header = soup.find("p", string=lambda t: table_name in t)
    if table_header:
        table = table_header.find_next("table")
        if not table:
            print(f"No {table_name} table found!")
            return None
        return table

    print(f"No {table_name} table header found!")
    return None

def get_relevant_rows(table):
    rows = table.find_all("tr")
    rows = rows[2:-1]  # Skip first two and last one row
    return rows

if __name__ == "__main__":
    main()