# Input files
sample_file = "sample.txt"
input_file = "input.txt"

cols = []

with open(sample_file, "r") as file:
    lines = [char.replace(".", " ").replace("^", "O") for char in file.readlines()]
    cols = (list(zip(*lines)))[:][:-1]


for col in cols:
    print(col)


# Part one logic
def part_01(data):
    lastLineEmpty = True
    while lastLineEmpty:
        for col in cols:
            for char in col:
                pass
                lastLineEmpty = False


print(f"A tachyon beam is split a total of {part_01(cols)} times.")
