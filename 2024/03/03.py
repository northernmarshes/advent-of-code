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
    operations = {}
    calculations = []
    sorted_calculations = {}
    valid_muls = []

    # Patterns
    pattern_mul = re.compile(r"mul\(\d{1,3},\d{1,3}\)")
    pattern_do = re.compile(r"do\(\)")
    pattern_dont = re.compile(r"don\'t")

    # Search for patterns
    muls = pattern_mul.finditer(data_line)
    dos = pattern_do.finditer(data_line)
    donts = pattern_dont.finditer(data_line)

    # Appending a dictionary
    for mul in muls:
        operations[mul.start()] = mul.group()
    for do in dos:
        operations[do.start()] = do.group()
    for dont in donts:
        operations[dont.start()] = dont.group()

    # Sorting the dictionary
    for key in sorted(operations.keys()):
        sorted_calculations[key] = operations[key]

    # Appendind a list of sorted calculations:
    for key, value in sorted_calculations.items():
        calculations.append(value)

    # Choosing only valid calculations
    valid = True
    for calc in calculations:
        if calc == "do()":
            valid = True
        elif calc == "don't":
            valid = False
        else:
            if valid:
                valid_muls.append(calc)

    # Calculations
    for mul in valid_muls:
        numbers = list(map(int, mul[4:-1].split(",")))
        result += math.prod(numbers)
    return result


print(
    part_2_regex(calc_lines), "is a sum of the results of the enabled multiplications."
)
