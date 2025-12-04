sec = "sequences.txt"
sample = "sample.txt"

sequences = []
dial_positions = []
for i in range(100):
    dial_positions.append(i)
zeros = []

with open(sample, "r") as file:
    lines = file.readlines()
    for line in lines:
        sequences.append(line[:-1])

index = dial_positions[50]

for sequence in sequences:
    if sequence[0] == "L":
        index = index - int(sequence[1:])
        print("left")
        print(index)
    else:
        print("right")
