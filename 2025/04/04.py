# Input files
sample = "sample.txt"
input = "input.txt"


# File loading
matrix = []
row = []
with open(sample, "r") as file:
    lines = file.readlines()
    for line in lines:
        for char in line[:-1]:
            row.append(char)
        matrix.append(row)
        row = []

# Changing characters for 0 and 1
for row in matrix:
    for char in range(len(row)):
        if row[char] == ".":
            row[char] = 0
        if row[char] == "@":
            row[char] = 1

# Printing the matrix
for r in matrix:
    print(r)


# Part one logic
def part_01(data):
    neighbors = []
    for row in range(len(data)):
        for index, value in enumerate(data[row]):
            if (
                row == 0
                or row == len(data) - 1
                or index == 0
                or index == len(data[row]) - 1
            ):
                new_neighbours = []
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
                    # right
                    data[row][index + 1],
                    # bottom
                    data[row + 1][index],
                    # left
                    data[row][index - 1],
                ]

                neighbors.append(
                    ["Index:", index, "Value:", value, "Neighbors:", new_neighbours]
                )
    return neighbors


rendered_neighbours = part_01(matrix)

for row in rendered_neighbours:
    print(row)
