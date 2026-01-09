import math
import re

sample_01_file = "sample_01.txt"
sample_02_file = "sample_02.txt"
input_file = "input.txt"

calc_lines = []

with open(input_file, "r") as f:
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
    result = 0
    calculations = []
    pattern = re.compile(r"(do\(\)){1}.*(mul\(\d{1,3},\d{1,3}\)){1}")
    for line in data:
        calc_line = pattern.findall(line)
        print(calc_line)


print("Result:", part_2_regex(calc_lines))
