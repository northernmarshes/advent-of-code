import math
import re

sample_01_file = "sample_01.txt"
sample_02_file = "sample_02.txt"
input_file = "input.txt"

calc_lines = []

with open(input_file, "r") as f:
    # with open(sample_02_file, "r") as f:
    lines = f.readlines()
    for line in lines:
        calc_lines.append(line[:-1])


def part_1_regex(data):
    result = 0
    calculations = []
    pattern = re.compile(r"mul\(\d{1,3},\d{1,3}\)")
    for line in data:
        calc_line = pattern.findall(line)
        for calc in calc_line:
            calculations.append(calc)
    for calculation in calculations:
        numbers = list(map(int, calculation[4:-1].split(",")))
        result += math.prod(numbers)
    return result


# print("Adding up the result of each instruction produces", part_1_regex(calc_lines))


def part_2_regex(data):
    data_line = "".join(data)
    result = 0
    calculations = {}
    sorted_calculations = {}
    objects = []

    # Patterns
    pattern_mul = re.compile(r"mul\(\d{1,3},\d{1,3}\)")
    pattern_do = re.compile(r"do\(\)")
    pattern_dont = re.compile(r"don\'t")

    # Search
    muls = pattern_mul.finditer(data_line)
    dos = pattern_do.finditer(data_line)
    donts = pattern_dont.finditer(data_line)

    # Appending
    for mul in muls:
        objects.append(mul)
    for do in dos:
        objects.append(do)
    for dont in donts:
        objects.append(dont)

    # Sorting
    #
    # Making a dictionary with a leading index
    for object in objects:
        start = object.start()
        group = object.group()
        calculations[start] = group

    for key in sorted(calculations.keys()):
        sorted_calculations[key] = calculations[key]

    for key, value in sorted_calculations.items():
        print(value)

    # Calculations:
    # for calc in calculations:
    # numbers = list(map(int, calc[4:-1].split(",")))
    # print("numbers", numbers)
    # result += math.prod(numbers)
    # return result


print("Result:", part_2_regex(calc_lines))


# Access to data in rematch: .group() .start() .end()
# pattern = re.compile(r"(do\(\)){1}.*(mul\(\d{1,3},\d{1,3}\)){1}")
# new_calc = str(start).zfill(5) + " " + group
