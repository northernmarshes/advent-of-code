sample_file = "sample.txt"
input_file = "input.txt"

matrix_cache = []


def parse_data(data: str):
    """Parsing the data"""
    if data not in matrix_cache:
        with open(data, "r") as f:
            lines = f.readlines()
            for line in lines:
                matrix_cache.append([char for char in line[:-1]])
    return matrix_cache


def rotate_matrix_45(matrix: list):
    """Rotating a matrix 45 degrees"""
    N = len(matrix)
    result = [["" for _ in range(2 * N - 1)] for _ in range(2 * N - 1)]
    for i in range(N):
        for j in range(N):
            new_i = i + j
            new_j = N - 1 + i - j
            result[new_i][new_j] = matrix[i][j]
    return result


def rotate_matrix_90(matrix: list):
    """Rotating a matrix 90 degrees"""
    new_matrix = []
    rotated = zip(*matrix[::-1])
    for line in rotated:
        new_matrix.append(list(line))
    return new_matrix


def part_1(data: str):
    """Part 1 logic"""
    matrix = parse_data(data)
    occurances = 0
    key = "XMAS"
    rotations = 0

    # Rotating matix 90 degrees
    while rotations <= 3:
        for line in matrix:
            occurances += ("".join(map(str, line))).count(key)
        matrix = rotate_matrix_90(matrix)
        rotations += 1
    rotations = 0

    # Rotating matrix 45 and then 90 degrees
    matrix = rotate_matrix_45(matrix)
    while rotations <= 3:
        for line in matrix:
            occurances += ("".join(map(str, line))).count(key)
        matrix = rotate_matrix_90(matrix)
        rotations += 1

    return occurances


print("XMAS appears", part_1(input_file), "times.")
