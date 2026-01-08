import math
import re

sample_file = "sample.txt"
input_file = "input.txt"

calc_lines = []

with open(sample_file, "r") as f:
    lines = f.readlines()
    for line in lines:
        calc_lines.append(line[:-1].split("mul"))


# def part_1(data):
#     result = 0
#     calculations = []
#     for line in data:
#         for calc in line:
#             if "(" and ")" in calc:
#                 calculations.append(calc)
#
#     multipliers = []
#     for calc in calculations:
#         print(calc)
#         inside = calc[calc.index("(") + 1 : calc.index(")")]
#         multipliers.append([int(x) for x in inside.split(",")])
#
#     for calc in multipliers:
#         result += math.prod(calc)
#     return result

# print(part_1(calc_lines))


def part_1_regex(data):
    result = 0
    calculations = []
    pattern = re.compile(r"\(\d+,\d+\)")
    for line in data:
        for calc in line[1:]:
            calculation = pattern.findall(calc)
            if calculation:
                calculations.append(calculation[0][1:-1])
    for calc in calculations:
        calc = [int(x) for x in calc.split(",")]
        result += math.prod(calc)
    return result


print(part_1_regex(calc_lines))
