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


for line in parse_data(sample_file)[0]:
    print(line)
print(parse_data(sample_file)[1])
