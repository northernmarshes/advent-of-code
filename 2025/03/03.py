# Input files
sample = "sample.txt"
input = "input.txt"

# Variables
banks = []
jolt_decimal = 0
jolt_units = 0
banks_joltage = []
total_joltage = []

# File loading
with open(sample, "r") as file:
    lines = file.readlines()
    for line in lines:
        banks.append(line[:-1])


# Part one logic
def part_01(data):
    for bank in data:
        jolt_decimal = max(int(x) for x in list(bank[:-1]))
        cut = list(bank).index(str(jolt_decimal))
        second_half = list(bank[cut + 1 :])

        jolt_units = max(second_half)
        joltage = int(str(jolt_decimal) + str(jolt_units))
        banks_joltage.append(joltage)
    total_joltage = sum(banks_joltage)
    return total_joltage


print(part_01(banks))


def part_02(data):
    for bank in data:
        initial_part = list(bank[:-12])
        print("initial", initial_part)

        jolt_12 = max(int(x) for x in list(initial_part))
        cut = list(bank).index(str(jolt_12))
        next_half = list(bank[cut + 1 : -10])
        print("next_half", next_half)

        jolt_11 = max(next_half)
        cut = next_half.index(str(jolt_11))
        next_half = list(bank[cut + 1 : -9])
        print("next_half", next_half)

        jolt_10 = max(next_half)
        cut = next_half.index(str(jolt_10))
        next_half = list(bank[cut + 1 : -8])
        print("next_half", next_half)

        jolt_09 = max(next_half)
        cut = next_half.index(str(jolt_09))
        next_half = list(bank[cut + 1 : -7])
        print("next_half", next_half)

        joltage = int(str(jolt_12) + str(jolt_11) + str(jolt_10) + str(jolt_09))
        print("joltage p2", joltage)
        banks_joltage.append(joltage)
        print("next_half", next_half)

    total_joltage = sum(banks_joltage)
    return total_joltage


print(part_02(banks))

# def part_02(data):
#     for bank in data:
#         jolt_index = 0
#         right_indent = -12
#         while right_indent < -1:
#             jolt = max(int(x) for x in list(bank[jolt_index:right_indent]))
#             print("jolt", jolt)
#             total_joltage.append(jolt)
#             total_joltage.append("break")
#             jolt_index = list(bank).index(str(jolt))
#             right_indent += 1
#     print(total_joltage)
#
#
# part_02(banks)
#

# # Part two logic
# def part_02_indexes(data):
#     indexes = []
#     bank_indexes = []
#     for bank in data:
#         count = 0
#         bank_list = []
#         for num in str(bank):
#             bank_list.append(num)
#         bank_list_copy = bank_list.copy()
#         while count < 12:
#             index = bank_list.index(max(bank_list))
#             indexes.append(index)
#             bank_list[index] = str(0)
#             count += 1
#         bank_indexes.append(indexes)
#         indexes = []
#         print(
#             [varx[1] for varx in enumerate(bank_list_copy) if varx[0] in [bank_indexes]]
#         )
#     return bank_indexes
#
#
# def part_02_values(data, ind):
#     pass
#
#
# # Working logic
# # number = 811111111111119
# number = 234234234234278
# numberlist = []
# for num in str(number):
#     numberlist.append(num)
# biggest_num = []
# biggest_num_index = []
# indexes = []
# count = 0
# numberlist_pure = numberlist.copy()
# while count < 12:
#     index = numberlist.index(max(numberlist))
#     indexes.append(index)
#     numberlist[index] = str(0)
#     count += 1
#
# indexes_sorted = sorted(indexes)
#
# print("indexes", indexes)
# print("indexes sorted", indexes_sorted)
#
#
# jolt = ""
# for num in range(len(numberlist_pure)):
#     if num in indexes_sorted:
#         jolt += numberlist_pure[num]
# print("joltge is:", jolt)


# print("Total output joltage from two batteries is:", part_01(banks))
# print("Total output joltage from nine batteries is:", part_02(banks))
# print(part_02_indexes(banks))

#
# number = 234234234234278
# numberlist = []
# total_joltage = []
# for num in str(number):
#     numberlist.append(int(num))
# print(numberlist)
# jolt_index = 0
# right_indent = -12
# while right_indent < 0:
#     jolt = max(int(x) for x in numberlist[jolt_index:right_indent])
#     jolt_index = numberlist.index((jolt)) + 1
#     print(jolt_index)
#     total_joltage.append(jolt)
#     right_indent += 1
# print(total_joltage)
