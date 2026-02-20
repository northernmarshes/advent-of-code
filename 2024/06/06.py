import numpy as np

input_file = "input.txt"
sample_file = "sample.txt"

data_cache = {}


def parse_data(data: str):
    """Parsing the data"""
    if data not in data_cache:
        with open(data, "r") as f:
            map_matrix = []
            chars = []
            lines = f.readlines()
            for line in lines:
                for char in line[:-1]:
                    if char == "^":
                        chars.append(char)
                    else:
                        chars.append(char)
                map_matrix.append(chars)
                chars = []
        data_cache[data] = map_matrix
    return data_cache[data]


def part_1(data: str):
    """Part 1 logic"""
    map_size = len(data)
    map_np = np.zeros((map_size, map_size))
    guard_on_map = True

    # Loading a numpy array
    for l_index, line in enumerate(data):
        for c_index, char in enumerate(line):
            if char == ".":
                map_np[l_index][c_index] = "0"
            elif char == "#":
                map_np[l_index][c_index] = "1"
            else:
                map_np[l_index][c_index] = "6"

    # Movement simulation
    while guard_on_map:
        for x, line in enumerate(map_np):
            for y, char in enumerate(line):
                if char == 6 and (map_np[x - 1, y] == 0 or map_np[x - 1, y] == 9):
                    map_np[x, y] = 9
                    map_np[x - 1, y] = 6
                if char == 6 and map_np[x - 1, y] == 1:
                    map_np = np.rot90(map_np)
                if char == 6 and x == 0:
                    map_np[x, y] = 9
                    guard_on_map = False

    # Counting positions
    c = np.count_nonzero(map_np == 9)
    return c


print(
    "The guard will visit",
    part_1(parse_data(input_file)),
    "distinct positions before leaving the mapped area",
)
