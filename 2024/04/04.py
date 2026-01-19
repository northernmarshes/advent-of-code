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
    N = len(matrix)
    result = [["" for _ in range(2 * N - 1)] for _ in range(2 * N - 1)]
    for i in range(N):
        for j in range(N):
            new_i = i + j
            new_j = N - 1 + i - j
            result[new_i][new_j] = matrix[i][j]
    return result


def part_1(data: str):
    matrix = parse_data(data)
    occurances = 0
    key = "XMAS"
    rotations = 0
    matrix = rotate_matrix(matrix)
    for line in matrix:
        print("".join(map(str, line)))
    # while rotations <= 7:
    #     for line in matrix:
    #         occurances += ("".join(map(str, line))).count(key)
    #     matrix = rotate_matrix(matrix)
    #     rotations += 1

    return occurances


print("XMAS appears", part_1(sample_file), "times.")
