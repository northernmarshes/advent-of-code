# Input files
import re
from typing import Counter


input_file = "input.txt"
sample_file = "sample.txt"

reports = []

# File loading
with open(sample_file, "r") as f:
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


# print(part_01(reports), "reports are safe.")


def part_02(data):
    # Variables
    ordered_reports = []
    unordered_reports = []
    differences_list = []
    safe = 0

    # Checking if a report is either all increasing or all decreasing
    for report in data:
        reversed = sorted(report, reverse=True)
        if report == sorted(report):
            ordered_reports.append(report)
        elif report == reversed:
            ordered_reports.append(report)
        else:
            unordered_reports.append(report)

    # Calculating differences between levels
    for report in ordered_reports:
        difference = [abs(report[i + 1] - report[i]) for i in range(len(report) - 1)]
        differences_list.append(difference)

    for report in differences_list:
        print(report)

    # Deleting a single mistake from each report
    for r, report in enumerate(differences_list):
        report_done = False
        for i, level in enumerate(report):
            if level > 3 or level == 0 and not report_done:
                print(
                    "deleting:", differences_list[r][i], "from row", differences_list[r]
                )
                differences_list[r][i - 1] += differences_list[r][i + 1]
                del differences_list[r][i + 1]
                del differences_list[r][i]

                report_done = True
    for report in differences_list:
        print(report)

    # Checking if a report has differences greater then 3
    for report in differences_list:
        res = all(level <= 3 and level > 0 for level in report)
        if res:
            safe += 1

    return safe


print(part_02(reports), "reports are actually safe.")
