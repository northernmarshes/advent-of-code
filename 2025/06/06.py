import math
import re

# Input files
sample_file = "sample.txt"
input_file = "input.txt"

# Variables
rows = []
all_solutions = []


# Part one logic
def part_01(data):
    solution = 0
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

    # Converting numbers to int
    for row in rows[:-1]:
        for i in range(len(row)):
            row[i] = int(row[i])
    # Rotating matrix
    data = [[data[j][i] for j in range(len(data))] for i in range(len(data[0]))]
    # Calculating
    for row in data:
        if row[-1] == "*":
            solution = math.prod(row[:-1])
            all_solutions.append(solution)
        if row[-1] == "+":
            solution = math.fsum(row[:-1])
            all_solutions.append(solution)
    all_solutions = round(math.fsum(all_solutions))
    return all_solutions


# print(part_01(rows), "is the grand total in part one.")


# Part two logic
def part_02(data):
    solution = 0
    all_solutions = []
    rows = []
    rows_joined = []
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

    # Converting numbers to int
    for row in rows:
        for i in range(len(row)):
            if row[i] != "+" and row[i] != "*":
                if row[i] != " ":
                    row[i] = int(row[i])
                if row[i] == " ":
                    row[i] = ""

    for row in rows:
        print(row)

    # numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # for row in range(len(rows)):
    #     if "*" in rows[row]:
    #         print("gwiazdka w rzędzie")
    #     if "+" in rows[row]:
    #         print("plus w rzędzie")
    #     if any(numbers == num for num in rows[row]):
    #         print("liczby!")

    # for index, value in enumerate(rows):

    # for row in rows:
    #     row = "".join(map(str, row))
    #     rows_joined.append(row)


print(part_02(sample_file), "is the grand total in part two.")
