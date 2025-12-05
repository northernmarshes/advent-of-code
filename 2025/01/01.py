input = "input.txt"
sample = "sample.txt"

# Variables
sequences = []
dial_positions = []
zeros_01 = 0
zeros_02 = 0
position = 50
rotations = 0

for i in range(100):
    dial_positions.append(i)

# File loading
with open(input, "r") as file:
    lines = file.readlines()
    for line in lines:
        sequences.append(line[:-1])

# Rotating logic
for sequence in sequences:
    # Rotating left
    if sequence[0] == "L":
        before = position
        click = int(sequence[1:])
        if click >= 100:
            # Counting zeros
            touches = int(str(click)[:-2])
            zeros_02 = zeros_02 + touches
            click = int(str(click)[1:])
        move = position - click
        position = dial_positions[move]

        # Counting zeros
        if position == 0:
            zeros_01, zeros_02 = zeros_01 + 1, zeros_02 + 1
        if before != 0 and before - click < 0:
            zeros_02 = zeros_02 + 1

    # Rotating right
    else:
        before = position
        click = int(sequence[1:])
        if click >= 100:
            # Counting zeros
            touches = int(str(click)[:-2])
            zeros_02 = zeros_02 + touches
            click = int(str(click)[1:])
        move = position + click
        if move >= 100:
            move = int(str(move)[1:])
        position = dial_positions[move]

        # Counting zeros
        if position == 0:
            zeros_01, zeros_02 = zeros_01 + 1, zeros_02 + 1
        if before != 0 and before + click > 100:
            zeros_02 = zeros_02 + 1

print(f"The total number of zero positions is: {zeros_01}")
print(f"The number dial touched zero is: {zeros_02}")
