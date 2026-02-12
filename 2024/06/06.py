sample_file = "sample.txt"
input_file = "input.txt"

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
    map = data[0]
    guard = data[1]
    position = []

    for x_index, line in enumerate(map):
        for y_index, char in enumerate(line):
            position = y_index, x_index
            print(position)


print(
    "The guard will visit",
    part_1(parse_data(sample_file)),
    "distinct positions before leaving the mapped area",
)
