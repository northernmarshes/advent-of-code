# Input files
sample = "sample.txt"
input = "input.txt"

# Variables
banks = []
jolt_decimal = 0
jolt_units = 0
banks_joltage = []
total_joltage = 0

# File loading
with open(input, "r") as file:
    lines = file.readlines()
    for line in lines:
        banks.append(line[:-1])

# Part one logic
for bank in banks:
    jolt_decimal = max(int(x) for x in list(bank[:-1]))
    cut = list(bank).index(str(jolt_decimal))
    second_half = list(bank[cut + 1 :])
    jolt_units = max(int(x) for x in list(second_half))
    joltage = int(str(jolt_decimal) + str(jolt_units))
    banks_joltage.append(joltage)

total_joltage = sum(banks_joltage)

print("Total output joltage is:", total_joltage)
