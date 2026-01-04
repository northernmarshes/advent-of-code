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
    safe = 0

    # Checking if a report is either all increasing or all decreasing
    for report in data:
        reversed = sorted(report, reverse=True)
        if report == sorted(report):
            ordered_reports.append(report)
            print("appending...", report)
        elif report == reversed:
            ordered_reports.append(report)
            print("appending...", report)
        else:
            unordered_reports.append(report)
            print("appending to unordered...", report)

    # Marking reports with no dampener used with "N"
    for report in ordered_reports:
        report.append("N")

    # Appending reports if deleting one level makes
    # it possible. Then marking the corrected report
    # by appending "Y" on the last index
    for report in unordered_reports:
        dampener = False
        for i, level in enumerate(report):
            if not dampener:
                report_model = report[:]
                report_model.remove(report[i])
                print(report_model)
                report_model_sorted_asc = sorted(report_model)
                print(report_model_sorted_asc)
                report_model_sorted_desc = sorted(report_model, reverse=True)
                print(report_model_sorted_desc)
                if (
                    report_model == report_model_sorted_asc
                    or report_model == report_model_sorted_desc
                ):
                    print("im removing", report[i])
                    report.remove(report[i])
                    report.append("Y")
                    ordered_reports.append(report)
                    unordered_reports.remove(report)
                    print("report", report, "has joined ordered ones")
                    dampener = True

    # Checking if the differences are withing norm
    for i, report in enumerate(ordered_reports):
        report = report[:-1]
        difference = [abs(report[i + 1] - report[i]) for i in range(len(report) - 1)]
        res = all(level <= 3 and level > 0 for level in difference)
        if res:
            print("differences in", report, "are", difference, "and its fine")
            safe += 1
        # Checking if removing a level can fix the report
        elif ordered_reports[i][-1] == "N":
            dampener = False
            for i, level in enumerate(report):
                if not dampener:
                    report_model = report[:]
                    report_model.remove(report[i])
                    difference = [
                        abs(report_model[i + 1] - report_model[i])
                        for i in range(len(report_model) - 1)
                    ]
                    print("differences in", report_model, "are", difference)
                    res = all(level <= 3 and level > 0 for level in difference)
                    if res:
                        safe += 1
                        print(
                            "differences in",
                            report_model,
                            "are",
                            difference,
                            "and its fine",
                        )
                        dampener = True

    return safe


print(part_02(reports), "reports are actually safe.")
