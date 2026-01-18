sample_file = "sample.txt"
input_file = "input.txt"

matrix_cache = []


def parse_data(data: str):
    if data not in matrix_cache:
        with open(data, "r") as f:
            lines = f.readlines()
            for line in lines:
                matrix_cache.append([char for char in line[:-1]])
    return matrix_cache


def rotate_matrix(matrix: list):
    pass
    # 90 degrees
    # return [list(reversed(col)) for col in zip(*matrix)]


def part_1(data: str):
    matrix = parse_data(data)
    occurances = 0
    key = "XMAS"
    for line in matrix:
        occurances += ("".join(map(str, line))).count(key)
    return occurances


print("XMAS appears", part_1(sample_file), "times.")
