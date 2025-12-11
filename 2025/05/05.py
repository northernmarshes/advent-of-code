from operator import itemgetter

# Input files
sample = "sample.txt"
input = "input.txt"

# Variables
scopes = []
ingredients = []
ranges = []
fresh_indexes = []

# File loading and appending lists
with open(sample, "r") as file:
    lines = file.readlines()
    for line in lines:
        if "-" in line:
            scope = []
            left = line.split("-")[0]
            right = line.split("-")[1]
            scope.append(int(left))
            scope.append(int(right))
            ranges.append(scope)
        if "-" not in line and line != "\n":
            ingredients.append(int(line[:-1]))


# Part one logic
def part_01(ingredients_f, ranges_f):
    fresh_indicator = 0
    fresh_ingredients = 0
    # Checking if an ingredient is in any range
    for ingredient in ingredients_f:
        fresh_indicator = 0
        for r in ranges_f:
            if ingredient in range(r[0], r[1] + 1):
                fresh_indicator += 1
        # If ingredient is in any range - append
        if fresh_indicator != 0:
            fresh_ingredients += 1
    return fresh_ingredients


# print(part_01(ingredients, ranges), "of the available ingredient IDs are fresh.")


# Part two logic
def part_02(ranges_f):
    sum = 0
    sorted_ranges = sorted(ranges_f, key=itemgetter(0))
    for r in sorted_ranges:
        print(r)
    for row in range(len(sorted_ranges)):
        for index, value in enumerate(sorted_ranges[row]):
            # All ranges except the last
            if index == 1 and row != (len(sorted_ranges) - 1):
                # Touching ranges
                if sorted_ranges[row][index] == sorted_ranges[row + 1][index - 1]:
                    print(sorted_ranges[row][index])
                    sum += (sorted_ranges[row][index]) - (sorted_ranges[row][index - 1])
                    print("touching line")
                    print("sum:", sum)
                    print("\n")
                # Normal ranges
                if sorted_ranges[row][index] < sorted_ranges[row + 1][index - 1]:
                    print(sorted_ranges[row][index])
                    sum += (
                        (sorted_ranges[row][index]) - (sorted_ranges[row][index - 1])
                    ) + 1
                    print("normal line")
                    print("sum:", sum)
                    print("\n")
                # Overlaping ranges
                if sorted_ranges[row][index] > sorted_ranges[row + 1][index - 1]:
                    print(sorted_ranges[row][index])
                    sum += (
                        (sorted_ranges[row][index]) - (sorted_ranges[row][index - 1])
                    ) + 1
                    sum += (
                        sorted_ranges[row + 1][index - 1] - sorted_ranges[row][index]
                    ) - 1
                    print("overlaping")
                    print("sum:", sum)
                    print("\n")
            # Last range
            if index == 1 and row == (len(sorted_ranges)) - 1:
                print("last index", sorted_ranges[row][index])
                print("row", row, "index", index)
                print("last row", sorted_ranges[row])
                sum += (
                    (sorted_ranges[row][index]) - (sorted_ranges[row][index - 1])
                ) + 1
                print(
                    "last range",
                    (sorted_ranges[row][index]) - (sorted_ranges[row][index - 1]),
                )
                print("last line")
                print("sum:", sum)
                print("\n")
                return sum


print(
    part_02(ranges),
    "ingredient IDs are considered to be fresh.",
)
