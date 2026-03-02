sample_file = "sample.txt"
input_file = "input.txt"


def parse_data(data):
    """Parsing the data"""

    cols = []
    with open(data, "r") as file:
        lines = [char.replace(".", " ") for char in file.readlines()]
        cols = list(map(list, zip(*lines)))[:][:-1]

    # Rotating the matrix
    cols = [[cols[j][i] for j in range(len(cols))] for i in range(len(cols[0]))]

    # Adding initial beam
    for ri, row in enumerate(cols):
        for ci, col in enumerate(row):
            if ri == 0 and col == "S":
                cols[ri + 1][ci] = "|"
    return cols


def part_01(data):
    """Part 1 logic"""

    count = 0
    split = 0
    while count < 12000:
        for ri, row in enumerate(data):
            for ci, col in enumerate(row):
                if ri < len(data) - 1 and col == "|" and data[ri + 1][ci] == " ":
                    data[ri + 1][ci] = "|"
                elif col == "^":
                    if data[ri - 1][ci] == "|":
                        data[ri][ci + 1] = "|"
                        data[ri][ci - 1] = "|"
                        data[ri][ci] = "@"
                        split += 1
            count += 1
    return split


print(f"A tachyon beam is split a total of {part_01(parse_data(input_file))} times.")


def part_02(data):
    """
    Part 2 logic. Spent lots of time reading about graphs and trees, went crazy
    for a while trying to figure it out. Eventually, looking at Yang Hui's triangle,
    it struck me how simple the problem actually was. I used only lists and no
    recursion which may be considered brutish way to do it and yet it allows the code
    to calculate 422102272495018 different paths in just 90 milliseconds.
    """

    count = 0
    split = 0

    # Simulating the beam
    while count < 12000:
        for ri, row in enumerate(data):
            for ci, col in enumerate(row):
                if ri < len(data) - 1 and col == "|" and data[ri + 1][ci] == " ":
                    data[ri + 1][ci] = "|"
                elif col == "^":
                    if data[ri - 1][ci] == "|":
                        data[ri][ci + 1] = "|"
                        data[ri][ci - 1] = "|"
                        data[ri][ci] = "@"
                        split += 1
            count += 1

    # Adding leaf nodes
    bottom_row = []
    for r in range(len(data[0])):
        bottom_row.append(" ")
    data.append(bottom_row)

    for r, row in enumerate(data):
        for c, col in enumerate(data[r]):
            if r == len(data) - 1 and data[r - 1][c] == "|":
                data[r][c] = "@"

    # Root count
    for ri, row in enumerate(data):
        for ci, col in enumerate(row):
            if ri == 2 and col == "@":
                data[ri][ci] = "1"

    # Counting ways to each node
    for r, row in enumerate(data):
        for c, col in enumerate(row):
            if data[r][c] == "@":
                node_paths = 0
                current_row = r
                # Adding paths for the whole beam length
                while data[current_row - 1][c] == "|":
                    # Calculating left parents
                    if (
                        data[current_row - 1][c - 1] != " "
                        and data[current_row - 1][c - 1] != "|"
                        and data[current_row - 1][c - 1] != "^"
                    ):
                        node_paths += int(data[current_row - 1][c - 1])
                    # Calculating right parents
                    if (
                        c < len(row) - 1
                        and data[current_row - 1][c + 1] != " "
                        and data[current_row - 1][c + 1] != "|"
                        and data[current_row - 1][c + 1] != "^"
                        and data[current_row - 1][c + 1] != "^"
                    ):
                        node_paths += int(data[current_row - 1][c + 1])

                    current_row = current_row - 1
                data[r][c] = str(node_paths)

    height = len(data)
    paths = 0
    for char in data[height - 1]:
        if char != " ":
            paths += int(char)
    return paths


print(
    f"A single tachyon particle end up on {part_02(parse_data(input_file))} timelines."
)
