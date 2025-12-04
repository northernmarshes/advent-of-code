import re

sample = "sample.txt"
input = "ranges.txt"

ranges = []
mischiefs = []
answer = 0

with open(input, "r") as file:
    line = str(file.readlines())[2:-4]
scopes = line.split(",")

for scope in scopes:
    edge_val = []
    r_bgn = (scope.split("-"))[0]
    r_end = (scope.split("-"))[1]
    edge_val.append(int(r_bgn))
    edge_val.append(int(r_end))
    ranges.append(edge_val)


def isRepeating(s):
    return re.fullmatch(r"(.*?)\1", s) is not None


for scope in ranges:
    for num in range(scope[0], scope[1] + 1):
        if isRepeating(str(num)):
            mischiefs.append(num)

for num in mischiefs:
    answer = answer + num

print(f"The sum of all invalid IDs is {answer}")
