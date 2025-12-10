# Input files
sample = "sample.txt"
input = "input.txt"


# File loading
matrix = []
pickedmap = []
row = []
with open(input, "r") as file:
    lines = file.readlines()
    for line in lines:
        for char in line[:-1]:
            row.append(char)
        matrix.append(row)
        row = []
    for line in lines:
        for char in line[:-1]:
            row.append(char)
        pickedmap.append(row)
        row = []


# Changing characters for 0 and 1
for row in matrix:
    for char in range(len(row)):
        if row[char] == ".":
            row[char] = 0
        if row[char] == "@":
            row[char] = 1

# Clearing pickedmap
for row in pickedmap:
    for char in range(len(row)):
        if row[char] == ".":
            row[char] = 0
        if row[char] == "@":
            row[char] = 0


# Part one logic
def part_01(data):
    accessablePapers = 0
    for row in range(len(data)):
        for index, value in enumerate(data[row]):
            if (
                row == 0
                or row == len(data) - 1
                or index == 0
                or index == len(data[row]) - 1
            ):
                new_neighbours = []
                # bottom right
                if index != len(data[index]) - 1 and row != len(data) - 1:
                    new_neighbours.append(data[row + 1][index + 1])
                # bottom left
                if index != 0 and row != len(data) - 1:
                    new_neighbours.append(data[row + 1][index - 1])
                # top right
                if index != len(data[index]) - 1 and row != 0:
                    new_neighbours.append(data[row - 1][index + 1])
                # top left
                if index != 0 and row != 0:
                    new_neighbours.append(data[row - 1][index - 1])
                # top
                if row != 0:
                    new_neighbours.append(data[(row - 1)][index])
                # right
                if index != len(data[index]) - 1:
                    new_neighbours.append(data[row][index + 1])
                # bottom
                if row != len(data) - 1:
                    new_neighbours.append(data[row + 1][index])
                # left
                if index != 0:
                    new_neighbours.append(data[row][index - 1])
            else:
                new_neighbours = [
                    # top
                    data[row - 1][index],
                    # top left
                    data[row - 1][index - 1],
                    # top right
                    data[row - 1][index + 1],
                    # right
                    data[row][index + 1],
                    # bottom
                    data[row + 1][index],
                    # bottom left
                    data[row + 1][index - 1],
                    # bottom right
                    data[row + 1][index + 1],
                    # left
                    data[row][index - 1],
                ]
            if value == 1 and sum(new_neighbours) < 4:
                accessablePapers += 1
    return accessablePapers


print(
    "In part one", part_01(matrix), "rolls of paper that can be accessed by a forklift."
)


# Part two logic
def part_02(data):
    paperisavialable = True
    collectedPapers_round = 0
    collectedPapers_overall = 0

    while paperisavialable:
        for row in range(len(data)):
            for index, value in enumerate(data[row]):
                if (
                    row == 0
                    or row == len(data) - 1
                    or index == 0
                    or index == len(data[row]) - 1
                ):
                    new_neighbours = []
                    # bottom right
                    if index != len(data[index]) - 1 and row != len(data) - 1:
                        new_neighbours.append(data[row + 1][index + 1])
                    # bottom left
                    if index != 0 and row != len(data) - 1:
                        new_neighbours.append(data[row + 1][index - 1])
                    # top right
                    if index != len(data[index]) - 1 and row != 0:
                        new_neighbours.append(data[row - 1][index + 1])
                    # top left
                    if index != 0 and row != 0:
                        new_neighbours.append(data[row - 1][index - 1])
                    # top
                    if row != 0:
                        new_neighbours.append(data[(row - 1)][index])
                    # right
                    if index != len(data[index]) - 1:
                        new_neighbours.append(data[row][index + 1])
                    # bottom
                    if row != len(data) - 1:
                        new_neighbours.append(data[row + 1][index])
                    # left
                    if index != 0:
                        new_neighbours.append(data[row][index - 1])
                else:
                    new_neighbours = [
                        # top
                        data[row - 1][index],
                        # top left
                        data[row - 1][index - 1],
                        # top right
                        data[row - 1][index + 1],
                        # right
                        data[row][index + 1],
                        # bottom
                        data[row + 1][index],
                        # bottom left
                        data[row + 1][index - 1],
                        # bottom right
                        data[row + 1][index + 1],
                        # left
                        data[row][index - 1],
                    ]
                if value == 1 and sum(new_neighbours) < 4:
                    collectedPapers_round += 1
                    pickedmap[row][index] = -1

        # Subtrackting picked papers
        data = [
            [data[i][j] + pickedmap[i][j] for j in range(len(data[0]))]
            for i in range(len(data))
        ]

        # Clearing pickedmap
        for row in pickedmap:
            for char in range(len(row)):
                if row[char] == -1:
                    row[char] = 0

        # Adding collected papers
        if collectedPapers_round != 0:
            collectedPapers_overall += collectedPapers_round
            collectedPapers_round = 0
        else:
            break

    return collectedPapers_overall


print(
    "In part two",
    part_02(matrix),
    "rolls of paper in total can be removed by the Elves and their forklifts.",
)
