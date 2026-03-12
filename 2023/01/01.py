input_file = "input.txt"
sample_file = "sample.txt"


def parse_data(data: str) -> list:
    words = []
    with open(data, "r") as f:
        lines = f.readlines()
        for line in lines:
            words.append(line[:-1])
    return words


def part_1(data: list) -> int:
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


print(part_1(parse_data(input_file)))
