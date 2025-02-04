from bs4 import BeautifulSoup
import assignment

def main():
    html_file = "algorai.html"
    with open(html_file, "r", encoding="utf-8") as f:
        html_content = f.read()

    soup = BeautifulSoup(html_content, "html.parser")

    class_name = find_class_name(soup)
    print("Class name:", class_name)

    assignment_table = find_table(soup, "Atsiskaitymas")
    if not assignment_table:
        return

    rows = get_relevant_rows(assignment_table)

    for row in rows:
        cells = row.find_all("td")
        name = cells[0].text
        for index in range(5, len(cells)):
            cell = cells[index]
            if cell.text == '*':
                assign_date = index - 5 + 1
            if cell.text == '0':
                due_date = index - 5 + 1
                task = assignment.Assignment(name, assign_date, due_date)
                assign_date = due_date

def find_class_name(soup: BeautifulSoup):
    meta_table = soup.find("table") # the table containing class name is the first table in doc
    class_name = meta_table.find("tr").find_all("td")[1].text
    return class_name

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