import regex as re

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
            sum += int(str(line_digits[0]) + str(line_digits[-1]))
    return sum


print(part_1(parse_data(input_file)), "is the sum of all of the calibration values.")


def part_2(data: list) -> int:
    """Part 2 logic"""
    sum = 0
    numbers = []

    # Looking for numbers
    for line in data:
        num = re.findall(
            r"\d|(?:one|two|three|four|five|six|seven|eight|nine)",
            line,
            overlapped=True,
        )
        numbers.append(num)

    # Type convertion
    for number in numbers:
        decimal = 0
        units = 0
        if number[0].isdigit():
            decimal = int(number[0])
        else:
            if number[0] == "zero":
                decimal = 0
            if number[0] == "one":
                decimal = 1
            if number[0] == "two":
                decimal = 2
            if number[0] == "three":
                decimal = 3
            if number[0] == "four":
                decimal = 4
            if number[0] == "five":
                decimal = 5
            if number[0] == "six":
                decimal = 6
            if number[0] == "seven":
                decimal = 7
            if number[0] == "eight":
                decimal = 8
            if number[0] == "nine":
                decimal = 9
        if number[-1].isdigit():
            units = int(number[-1])
        else:
            if number[-1] == "zero":
                units = 0
            if number[-1] == "one":
                units = 1
            if number[-1] == "two":
                units = 2
            if number[-1] == "three":
                units = 3
            if number[-1] == "four":
                units = 4
            if number[-1] == "five":
                units = 5
            if number[-1] == "six":
                units = 6
            if number[-1] == "seven":
                units = 7
            if number[-1] == "eight":
                units = 8
            if number[-1] == "nine":
                units = 9
        sum += decimal * 10 + units
    return sum


print(part_2(parse_data(input_file)), "is the sum of all of the calibration values.")
