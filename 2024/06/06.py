import numpy as np

input_file = "input.txt"
sample_file = "sample.txt"

data_cache = {}


def parse_data(data: str):
    """Parsing the data"""
    if data not in data_cache:
        with open(data, "r") as f:
            lines = f.readlines()
            map_size = len(lines[0][:-1])
            map_np = np.zeros((map_size, map_size))

            # Loading a numpy array
            for l_index, line in enumerate(lines):
                for c_index, char in enumerate(line[:-1]):
                    if char == ".":
                        map_np[l_index][c_index] = "0"
                    elif char == "#":
                        map_np[l_index][c_index] = "1"
                    else:
                        map_np[l_index][c_index] = "6"
        data_cache[data] = map_np
    return data_cache[data]


def part_1(data):
    """Part 1 logic"""
    map_np = data
    guard_on_map = True

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
    part_1(parse_data(sample_file)),
    "distinct positions before leaving the mapped area",
)


def part_2(data):
    """Part 2 logic"""
    map_np = data
    pass


print(
    "We could choose",
    part_2(parse_data(sample_file)),
    "different positions for this obstruction",
)
