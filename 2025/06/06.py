import math
import re

# Input files
sample_file = "sample.txt"
input_file = "input.txt"


# Part one logic
def part_01(data):
    solution = 0
    rows = []
    all_solutions = []
    # File loading and appending lists
    with open(data, "r") as file:
        lines = file.readlines()
        for line in lines:
            if " " in line:
                re_compile = re.compile(r"\s+")
                row = re_compile.sub(" ", line).strip()
                row = row.split(" ")
                rows.append(row)

    # Converting numbers to int
    for row in rows[:-1]:
        for i in range(len(row)):
            row[i] = int(row[i])
    # Rotating matrix
    lines = [[rows[j][i] for j in range(len(rows))] for i in range(len(rows[0]))]
    # Calculating
    for row in lines:
        if row[-1] == "*":
            solution = math.prod(row[:-1])
            all_solutions.append(solution)
        if row[-1] == "+":
            solution = math.fsum(row[:-1])
            all_solutions.append(solution)
    all_solutions = round(math.fsum(all_solutions))
    return all_solutions


print(part_01(input_file), "is the grand total in part one.")


# Part two logic
def part_02(data):
    all_solutions = []
    rows = []
    lines = []

    # File loading and appending lists
    with open(data, "r") as file:
        lines = file.readlines()
        for line in lines:
            row = []
            for i in range(len(line[:-1])):
                row.append(line[i])
            rows.append(row)

    # Rotating matrix
    rows = [[rows[j][i] for j in range(len(rows))] for i in range(len(rows[0]))]

    # Joining rotated digits into numbers and stripping spaces
    for row in rows:
        lines.append(("".join(map(str, row))).strip().replace(" ", ""))

    # Adding empty line in the end
    lines.append("")

    # Calculating
    for index, row in enumerate(lines):
        try:
            if (
                row != ""
                and row[-1] == "+"
                or row[-1] == "*"
                and lines[index + 1] != ""
            ):
                numbers = []
                numbers.append(int(row[:-1]))
                numbers.append(int(lines[index + 1]))
                if lines[index + 2] != "":
                    numbers.append(int(lines[index + 2]))
                    if lines[index + 3] != "":
                        numbers.append(int(lines[index + 3]))
                if row[-1] == "+":
                    all_solutions.append(math.fsum(numbers))
                if row[-1] == "*":
                    all_solutions.append(math.prod(numbers))
        except IndexError:
            pass
    solutions_sum = round(math.fsum(all_solutions))
    return solutions_sum


print(part_02(input_file), "is the grand total in part two.")
