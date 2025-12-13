import math
import re

# Input files
sample_file = "sample.txt"
input_file = "input.txt"

# Variables
rows = []
all_solutions = []

# File loading and appending lists
with open(input_file, "r") as file:
    lines = file.readlines()
    for line in lines:
        if " " in line:
            re_compile = re.compile(r"\s+")
            row = re_compile.sub(" ", line).strip()
            row = row.split(" ")
            rows.append(row)

for row in rows[:-1]:
    for i in range(len(row)):
        row[i] = int(row[i])


# Part one logic
def part_01(data):
    solution = 0
    all_solutions = []
    data = [[data[j][i] for j in range(len(data))] for i in range(len(data[0]))]
    for row in data:
        if row[-1] == "*":
            print("row", row[:-1])
            solution = math.prod(row[:-1])
            print("multiplication", solution)
            all_solutions.append(solution)
            print("\n")
        if row[-1] == "+":
            print("row", row[:-1])
            solution = math.fsum(row[:-1])
            all_solutions.append(solution)
            print("sum", solution)
            print("\n")
    print(all_solutions)
    print("\n")
    all_solutions = round(math.fsum(all_solutions))
    return all_solutions


print(part_01(rows), "is the grand total.")
