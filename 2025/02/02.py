sample = "sample.txt"
input = "ranges.txt"
ranges = []

with open(sample, "r") as file:
    line = str(file.readlines())[2:-4]
scopes = line.split(",")
for scope in scopes:
    edge_val = []
    r_bgn = (scope.split("-"))[0]
    r_end = (scope.split("-"))[1]
    edge_val.append(int(r_bgn))
    edge_val.append(int(r_end))
    ranges.append(edge_val)

elfs_ids = []


def isRepeating(s):
    return s in (s + s)[1:-1]


for num in range(ranges[0][0], (ranges[0][1] + 1)):
    if isRepeating(str(num)) == True:
        elfs_ids.append(num)


print(elfs_ids)


# print(elfs_ids)
