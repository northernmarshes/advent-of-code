import re

# Input files
sample = "sample.txt"
input = "ranges.txt"

# Variables
ranges = []
mischiefs_01 = []
mischiefs_02 = []
answer_01 = 0
answer_02 = 0

# File loading
with open(input, "r") as file:
    line = str(file.readlines())[2:-4]
scopes = line.split(",")

# List filling
for scope in scopes:
    edge_val = []
    r_bgn = (scope.split("-"))[0]
    r_end = (scope.split("-"))[1]
    edge_val.append(int(r_bgn))
    edge_val.append(int(r_end))
    ranges.append(edge_val)


# Part 1 logic
def isRepeating_twice(s):
    return re.fullmatch(r"(.*?)\1", s) is not None


# Part 2 logic
def isRepeating_more_times(s):
    return re.fullmatch(r"(.*?)\1+", s) is not None


# First answer calculation
for scope in ranges:
    for num in range(scope[0], scope[1] + 1):
        if isRepeating_twice(str(num)):
            mischiefs_01.append(num)
for num in mischiefs_01:
    answer_01 = answer_01 + num

# Second answer calculation
for scope in ranges:
    for num in range(scope[0], scope[1] + 1):
        if isRepeating_more_times(str(num)):
            mischiefs_02.append(num)
for num in mischiefs_02:
    answer_02 = answer_02 + num

# Output
print(f"The sum of all invalid IDs for part one is {answer_01}")
print(f"The sum of all invalid IDs for part two is {answer_02}")
