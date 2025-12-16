# Input files
sample_file = "sample.txt"
input_file = "input.txt"

cols = []

with open(sample_file, "r") as file:
    lines = [char.replace(".", " ") for char in file.readlines()]
    cols = list(map(list, zip(*lines)))[:][:-1]

# Rotating the matrix
cols = [[cols[j][i] for j in range(len(cols))] for i in range(len(cols[0]))]

# Adding initial beam
for ri, row in enumerate(cols):
    for ci, col in enumerate(row):
        if ri == 0 and col == "S":
            cols[ri + 1][ci] = "|"


# Part one logic
def part_01(data):
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


# print(f"A tachyon beam is split a total of {part_01(cols)} times.")


def part_02(data):
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

    # for r, row in enumerate(data):
    #     for c, col in enumerate(data[r]):
    #         if data[r][c] == "K":
    #             del data[r]

    for row in data:
        print(row)


print(f"A single tachyon particle end up on {part_02(cols)} timelines.")
