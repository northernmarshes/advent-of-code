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


# print(part_01(reports), "reports are safe.")


def part_02(data):
    safe = 0
    for report in data:
        dampener = False
        model_01 = report[:]
        limit = False
        model_01_sorted_asc = sorted(model_01)
        model_01_sorted_desc = sorted(model_01, reverse=True)
        difference = [
            abs(model_01[i + 1] - model_01[i]) for i in range(len(model_01) - 1)
        ]
        limit = all(level <= 3 and level > 0 for level in difference)
        if model_01 == model_01_sorted_asc or model_01 == model_01_sorted_desc:
            if limit:
                print(
                    "Differences in",
                    model_01,
                    "are",
                    difference,
                    "and it's SAFE regardless.",
                )
                # data.remove(report)
                safe += 1
            else:
                for i, level in enumerate(report):
                    if not dampener:
                        model_02 = report[:]
                        del model_02[i]
                        print("Trying to pass with:", model_02)
                        model_02_sorted_asc = sorted(model_02)
                        model_02_sorted_desc = sorted(model_02, reverse=True)
                        difference_02 = [
                            abs(model_02[d + 1] - model_02[d])
                            for d in range(len(model_02) - 1)
                        ]
                        limit_02 = all(
                            level <= 3 and level > 0 for level in difference_02
                        )
                        print("limit", difference_02, "and it's:", limit_02)
                        if limit_02 and (
                            model_02 == model_02_sorted_asc
                            or model_02 == model_02_sorted_desc
                        ):
                            safe += 1
                            print(
                                "Differences in",
                                model_02,
                                "are",
                                difference_02,
                                "because we removed",
                                report[i],
                                "and it's SAFE.",
                            )
                            dampener = True
        else:
            for i, level in enumerate(report):
                if not dampener:
                    model_02 = report[:]
                    del model_02[i]
                    print("Trying to pass with:", model_02)
                    model_02_sorted_asc = sorted(model_02)
                    model_02_sorted_desc = sorted(model_02, reverse=True)
                    difference_02 = [
                        abs(model_02[d + 1] - model_02[d])
                        for d in range(len(model_02) - 1)
                    ]
                    limit_02 = all(level <= 3 and level > 0 for level in difference_02)
                    print("limit", difference_02, "and it's:", limit_02)
                    if limit_02 and (
                        model_02 == model_02_sorted_asc
                        or model_02 == model_02_sorted_desc
                    ):
                        safe += 1
                        print(
                            "Differences in",
                            model_02,
                            "are",
                            difference_02,
                            "because we removed",
                            report[i],
                            "and it's SAFE.",
                        )
                        dampener = True

    return safe


print(part_02(reports), "reports are actually safe.")
