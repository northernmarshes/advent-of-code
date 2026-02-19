import numpy as np

input_file = "input.txt"
sample_file = "sample.txt"

data_cache = {}


def parse_data(data: str):
    """Parsing the data"""
    if data not in data_cache:
        with open(data, "r") as f:
            map_matrix = []
            guard_position = []
            chars = []
            lines = f.readlines()
            for line in lines:
                for char in line[:-1]:
                    if char == "^":
                        chars.append(char)
                        guard_position = (
                            (lines.index(line)),
                            (chars.index(char)),
                        )
                    else:
                        chars.append(char)
                map_matrix.append(chars)
                chars = []
        data_cache[data] = map_matrix, guard_position
    return data_cache[data]


def part_1(data: str):
    """Part 1 logic"""
    map_np = np.zeros((10, 10))

    for l_index, line in enumerate(data[0]):
        for c_index, char in enumerate(line):
            if char == ".":
                map_np[l_index][c_index] = "0"
            elif char == "#":
                map_np[l_index][c_index] = "1"
            else:
                map_np[l_index][c_index] = "6"
    print(map_np)


print(
    "The guard will visit",
    part_1(parse_data(sample_file)),
    "distinct positions before leaving the mapped area",
)
