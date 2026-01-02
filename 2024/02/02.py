# Input files
input_file = "input.txt"
sample_file = "sample.txt"

reports = []

# File loading
with open(input_file, "r") as f:
    lines = f.readlines()
    for line in lines:
        line_int = list(map(int, (line[:-1]).split(" ")))
        reports.append(line_int)


def part_01(data):
    # Variables
    ordered_reports = []
    differences_list = []
    safe = 0

    # Checking if a report is either all increasing or all decreasing
    for report in data:
        reversed = sorted(report, reverse=True)
        if report == sorted(report):
            ordered_reports.append(report)
        elif report == reversed:
            ordered_reports.append(report)

    # Calculating differences between levels
    for report in ordered_reports:
        difference = [abs(report[i + 1] - report[i]) for i in range(len(report) - 1)]
        differences_list.append(difference)

    # Checking if a report has differences greater then 3
    for report in differences_list:
        res = all(level <= 3 and level > 0 for level in report)
        if res:
            safe += 1
    return safe


print(part_01(reports), "reports are safe.")
