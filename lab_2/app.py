def read_input_file(file_path):
    reports = []
    with open(file_path, 'r') as file:
        for line in file:
            reports.append([int(x) for x in line.split()])
    return reports


def is_safe(report):
    increasing = all(report[i] < report[i + 1] and 1 <= report[i + 1] - report[i] <= 3 for i in range(len(report) - 1))
    decreasing = all(report[i] > report[i + 1] and 1 <= report[i] - report[i + 1] <= 3 for i in range(len(report) - 1))
    return increasing or decreasing

def can_become_safe(report):
    for i in range(len(report)):
        modified_report = report[:i] + report[i + 1:]
        if is_safe(modified_report):
            return True
    return False

file_path = "input_2.txt"
reports = read_input_file(file_path)
safe_reports = sum(1 for report in reports if is_safe(report))
safe_reports_with_removal = sum(1 for report in reports if is_safe(report) or can_become_safe(report))
print("Safe Reports:", safe_reports)
print("Safe Reports with оne removal:", safe_reports_with_removal)