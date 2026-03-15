import re

input_file = "input.txt"
sample_file = "sample.txt"
sample_02_file = "sample_02.txt"


def parse_data(data: str) -> list:
    """Parsing the data"""
    words = []
    with open(data, "r") as f:
        lines = f.readlines()
        for line in lines:
            words.append(line[:-1])
    return words


def part_1(data: list) -> int:
    """Part 1 logic"""
    lines = data
    sum = 0
    for line in lines:
        line_digits = []
        for char in line:
            if char.isdigit():
                line_digits.append(int(char))
        if line_digits != []:
            print(line_digits[0])
            print(line_digits[-1])
            sum += int(str(line_digits[0]) + str(line_digits[-1]))
    return sum


# print(part_1(parse_data(input_file)))


def part_2(data: list) -> int:
    """Part 2 logic"""
    lines = data
    sum = 0

    digits_strings = [
        [
            "zero",
            "one",
            "two",
            "three",
            "four",
            "six",
            "seven",
            "eight",
            "nine",
        ],
        [
            "0",
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
        ],
    ]

    digits_indexes = []
    for index, line in enumerate(lines):
        line_indexes = []
        for digit in digits_strings[0]:
            pair = []
            if digit in line:
                pair.append(int(line.index(digit)))
                pair.append(int(digits_strings[1][index]))
            line_indexes.append(pair)
        digits_indexes.append(line_indexes)

    for index in digits_indexes:
        print(index)
    # for line in lines:
    # print(line)

    # sum = part_1(lines)

    return sum


print(part_2(parse_data(sample_02_file)))
