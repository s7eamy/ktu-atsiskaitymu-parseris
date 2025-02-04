from bs4 import BeautifulSoup
import assignment
import datetime
import csv
import argparse

def main():
    html_file, start_date = get_input()
    with open(html_file, "r", encoding="utf-8") as f:
        html_content = f.read()

    soup = BeautifulSoup(html_content, "html.parser")

    class_name = find_class_name(soup)
    print("Class name:", class_name)

    assignment_table = find_table(soup, "Atsiskaitymas")
    if not assignment_table:
        return

    rows = get_relevant_rows(assignment_table)

    assignments = parse_assignments(rows)
    print(f"Contains a total of {len(assignments)} assignments:")
    evaluate_start_date(assignments, start_date)
    for assignment in assignments:
        print(f"{assignment.name} assigned on {assignment.assign_date} and due on {assignment.due_date}")

    export_to_csv(class_name, assignments, start_date)

def get_input():
    parser = argparse.ArgumentParser(description="Parse assignments from html file")
    parser.add_argument("html_file", help="Path to the KTU class program (liet. modulio kortelė) html file")
    parser.add_argument("start_date", help="Start date of the course in format YYYY-MM-DD")
    args = parser.parse_args()
    html_file = args.html_file
    start_date = datetime.datetime.strptime(args.start_date, "%Y-%m-%d").date()
    return html_file, start_date

def find_class_name(soup: BeautifulSoup):
    meta_table = soup.find("table") # the table containing class name is the first table in doc
    class_name = meta_table.find("tr").find_all("td")[1].text.strip()
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

def parse_assignments(rows):
    assignments: list[assignment.Assignment] = []
    for row in rows:
        cells = row.find_all("td")
        name = cells[0].text.strip()
        for index in range(5, len(cells)):
            cell = cells[index]
            if cell.text == '*':
                assign_date = index - 5 + 1
            if cell.text == '0':
                due_date = index - 5 + 1
                task = assignment.Assignment(name, assign_date, due_date)
                assignments.append(task)
                assign_date = due_date
    return assignments

def evaluate_start_date(assignments: list[assignment.Assignment], start_date: datetime.date):
    for assignment in assignments:
        assignment.assign_date = start_date + datetime.timedelta(weeks=assignment.assign_date - 1)
        assignment.due_date = start_date + datetime.timedelta(weeks=assignment.due_date - 1)

def export_to_csv(class_name, assignments: list[assignment.Assignment], start_date):
    with open("assignments.csv", "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile, delimiter=";")
        # optional header
        for a in assignments:
            writer.writerow([
                class_name,
                a.name,
                a.weight,
                # example assumes 'due_date' is weeks offset from start_date
                a.due_date.strftime("%Y/%m/%d")
            ])

if __name__ == "__main__":
    main()