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


# def part_02(data):
#     count = 0
#     split = 0
#     while count < 12000:
#         for ri, row in enumerate(data):
#             for ci, col in enumerate(row):
#                 if ri < len(data) - 1 and col == "|" and data[ri + 1][ci] == " ":
#                     data[ri + 1][ci] = "|"
#                 elif col == "^":
#                     if data[ri - 1][ci] == "|":
#                         data[ri][ci + 1] = "|"
#                         data[ri][ci - 1] = "|"
#                         data[ri][ci] = "@"
#                         split += 1
#             count += 1
#
#     # Adding leaf nodes
#     bottom_row = []
#     for r in range(len(data[0])):
#         bottom_row.append(" ")
#     data.append(bottom_row)
#
#     for r, row in enumerate(data):
#         for c, col in enumerate(data[r]):
#             if r == len(data) - 1 and data[r - 1][c] == "|":
#                 data[r][c] = "@"
#
#     # Initial count
#     for ri, row in enumerate(cols):
#         for ci, col in enumerate(row):
#             if ri == 2 and col == "@":
#                 cols[ri][ci] = "1"
#
#     # Counting ways to each node
#     for r, row in enumerate(data):
#         for c, col in enumerate(row):
#             if data[r][c] == "@":
#                 node_paths = 0
#                 if (
#                     data[r - 2][c - 1] != " "
#                     and data[r - 2][c - 1] != "|"
#                     and data[r - 2][c - 1] != "^"
#                 ):
#                     node_paths += int(data[r - 2][c - 1])
#                 if (
#                     c < len(row) - 1
#                     and data[r - 2][c + 1] != " "
#                     and data[r - 2][c + 1] != "|"
#                     and data[r - 2][c + 1] != "^"
#                     and data[r - 2][c + 1] != "^"
#                 ):
#                     node_paths += int(data[r - 2][c + 1])
#                 data[r][c] = str(node_paths)
#
#     for row in data:
#         print(row)
#
#
# print(f"A single tachyon particle end up on {part_02(cols)} timelines.")
#


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def dfs_recursive(node):
    if node is None:
        print("path!")
        return
    print(node.value)
    dfs_recursive(node.left)
    dfs_recursive(node.right)


node_2 = Node(2)
node_3 = Node(3)
node_4 = Node(4)
node_5 = Node(5)

node_2.left = node_3
node_2.right = node_4
node_3.left = node_5


dfs_recursive(node_2)
