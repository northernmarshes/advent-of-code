sec = "sequences.txt"
sample = "sample.txt"

sequences = []
dial_positions = []
for i in range(100):
    dial_positions.append(i)
zeros = 0

with open(sample, "r") as file:
    lines = file.readlines()
    for line in lines:
        sequences.append(line[:-1])

previous = 50
for sequence in sequences:
    if sequence[0] == "L":
        new_step = dial_positions[previous - int(sequence[1:])]
        print(new_step)
        previous = new_step
        if previous == 0:
            zeros = zeros + 1
    else:
        move = previous + int(sequence[1:])
        if move >= 100:
            move = int(str(move)[1:])
        new_step = move
        print(new_step)
        previous = new_step
        if previous == 0:
            zeros = zeros + 1
print(f"The total number of zero positions is: {zeros}")
