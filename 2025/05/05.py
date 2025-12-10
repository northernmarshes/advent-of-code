# Input files
sample = "sample.txt"
input = "input.txt"

# Variables
scopes = []
ingredients = []
ranges = []
fresh_indexes = []

# File loading and appending lists
with open(input, "r") as file:
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


print(part_01(ingredients, ranges), "of the available ingredient IDs are fresh.")
