# Input files
sample = "sample.txt"
input = "input.txt"

# Variables
banks = []
jolt_decimal = 0
jolt_units = 0
banks_joltage = []
total_joltage = 0
nine_batteries = []

# File loading
with open(sample, "r") as file:
    lines = file.readlines()
    for line in lines:
        banks.append(line[:-1])


# Part one logic
def part_01(data):
    for bank in data:
        jolt_decimal = max(bank[:-1])
        cut = list(bank).index(str(jolt_decimal))
        second_half = list(bank[cut + 1 :])
        jolt_units = max(second_half)
        joltage = int(str(jolt_decimal) + str(jolt_units))
        banks_joltage.append(joltage)
    total_joltage = sum(banks_joltage)
    return total_joltage


# Part two logic
def part_02_indexes(data):
    indexes = []
    bank_indexes = []
    for bank in data:
        count = 0
        bank_list = []
        for num in str(bank):
            bank_list.append(num)
        bank_list_copy = bank_list.copy()
        while count < 12:
            index = bank_list.index(max(bank_list))
            indexes.append(index)
            bank_list[index] = str(0)
            count += 1
        bank_indexes.append(indexes)
        indexes = []
        print(
            [varx[1] for varx in enumerate(bank_list_copy) if varx[0] in [bank_indexes]]
        )
    return bank_indexes


def part_02_values(data, ind):
    pass


# Working logic
# number = 811111111111119
number = 234234234234278
numberlist = []
for num in str(number):
    numberlist.append(num)
biggest_num = []
biggest_num_index = []
indexes = []
count = 0
numberlist_pure = numberlist.copy()
while count < 12:
    index = numberlist.index(max(numberlist))
    indexes.append(index)
    numberlist[index] = str(0)
    count += 1

indexes_sorted = sorted(indexes)

print("indexes", indexes)
print("indexes sorted", indexes_sorted)


jolt = ""
for num in range(len(numberlist_pure)):
    if num in indexes_sorted:
        jolt += numberlist_pure[num]
print("joltge is:", jolt)


# print("Total output joltage from two batteries is:", part_01(banks))
# print("Total output joltage from nine batteries is:", part_02(banks))
print(part_02_indexes(banks))
