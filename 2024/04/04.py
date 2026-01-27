sample_file = "sample.txt"
input_file = "input.txt"

matrix_cache = {}


def parse_data(data: str):
    """Parsing the data"""
    if data not in matrix_cache:
        with open(data, "r") as f:
            matrix = []
            lines = f.readlines()
            for line in lines:
                matrix.append([char for char in line[:-1]])
        matrix_cache[data] = matrix
    return matrix_cache[data]


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


def part_2(data: str):
    """Part 2 logic"""
    matrix = parse_data(data)
    occurances = 0
    rotations = 0

    # Rotating matrix 3 times looking for X-MAS
    while rotations <= 3:
        for r, line in enumerate(matrix[:-1]):
            for c, char in enumerate(line[:-1]):
                if (
                    matrix[r][c] == "A"
                    and matrix[r - 1][c - 1] == "M"
                    and matrix[r - 1][c + 1] == "M"
                    and matrix[r + 1][c - 1] == "S"
                    and matrix[r + 1][c + 1] == "S"
                    and c != 0
                ):
                    occurances += 1
        matrix = rotate_matrix_90(matrix)
        rotations += 1
    return occurances


print("The actual X-MAS appears", part_2(input_file), "times.")
