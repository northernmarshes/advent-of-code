import math

sample_file = "sample.txt"
input_file = "input.txt"

calc_lines = []

with open(sample_file, "r") as f:
    lines = f.readlines()
    for line in lines:
        calc_lines.append(line[:-1].split("mul"))


def part_1(data):
    result = 0
    calculations = []
    for line in data:
        for calc in line:
            if "(" and ")" in calc:
                calculations.append(calc)

    multipliers = []
    for calc in calculations:
        inside = calc[calc.index("(") + 1 : calc.index(")")]
        multipliers.append([int(x) for x in inside.split(",")])
    print()

    for calc in multipliers:
        result += math.prod(calc)
    return result


print(part_1(calc_lines))
