from bs4 import BeautifulSoup
import urllib.request 
import assignment
import datetime
import csv
import argparse

def main():
    class_codes, start_dates = get_input()
    if not class_codes or not start_dates:
        return
    print(f"Parsing {len(class_codes)} classes...")
    print("----------------------------------------")
    for i in range(len(class_codes)):
        parse_class(class_codes[i], start_dates[i])
        print("----------------------------------------")

def parse_class(class_code, start_date):
    url = f"https://uais.cr.ktu.lt/ktuis/stp_report_ects.mdl_ml?p_kodas={class_code}&p_year=2024&p_lang=LT"
    html_content = urllib.request.urlopen(url).read()

    soup = BeautifulSoup(html_content, "html.parser")

    try:
        class_name = find_class_name(soup)
    except:
        print("Failed to parse class name")
        print("Check if the class code is correct")
        return
    print("Class name:", class_name)

    assignment_table = find_table(soup, "Atsiskaitymas")
    if not assignment_table:
        return

    rows = get_relevant_rows(assignment_table)

    assignments = parse_assignments(rows)
    print(f"Contains a total of {len(assignments)} assignments:")
    evaluate_start_date(assignments, start_date)
    for assignment in assignments:
        print(f"{assignment.name} ({assignment.weight*100}%) assigned on {assignment.assign_date} and due on {assignment.due_date}")

    export_to_csv(class_name, assignments, start_date)

def get_input():
    parser = argparse.ArgumentParser(description="Get KTU class assigment data")
    parser.add_argument("-c", "--class_codes", help="Code for the class (for exampe, T120B162). Can specify multiple codes separated by spaces", nargs='+', required=True)
    parser.add_argument("-d", "--start_dates", help="Start date of the course in format YYYY-MM-DD. Can specify multiple. If multiple, the number of dates must match the number of class codes and their order", nargs='+', required=True)
    args = parser.parse_args()
    class_codes = args.class_codes
    start_dates = [datetime.datetime.strptime(start_date, "%Y-%m-%d").date() for start_date in args.start_dates]
    if len(class_codes) != len(start_dates):
        print("Number of class codes and start dates must match!")
        return None, None
    return class_codes, start_dates

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
        assigns = parse_row(row)
        assignments.extend(assigns)
    return assignments

def parse_row(row):
    assigns: list[assignment.Assignment] = []
    cells = row.find_all("td")
    name = cells[0].text.strip()
    weight = int(cells[4].text.strip())
    for index in range(5, len(cells)):
        cell = cells[index]
        if cell.text == '*':
            assign_date = index - 5 + 1
        if cell.text == '0':
            due_date = index - 5 + 1
            task = assignment.Assignment(name, assign_date, due_date)
            assigns.append(task)
            assign_date = due_date
    
    # recalculate weights
    for assign in assigns:
        assign.weight = round(weight / len(assigns) / 100, 4)
    return assigns

def evaluate_start_date(assignments: list[assignment.Assignment], start_date: datetime.date):
    for assignment in assignments:
        assignment.assign_date = start_date + datetime.timedelta(weeks=assignment.assign_date - 1)
        assignment.due_date = start_date + datetime.timedelta(weeks=assignment.due_date - 1)

def export_to_csv(class_name, assignments: list[assignment.Assignment], start_date):
    with open(f"{class_name.replace(' ', '-').lower()}.csv", "w", newline="", encoding="utf-8") as csvfile:
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