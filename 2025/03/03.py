# Input files
sample = "sample.txt"
input = "input.txt"


# File loading
banks = []
with open(input, "r") as file:
    lines = file.readlines()
    for line in lines:
        banks.append(line[:-1])


# Part one logic
def part_01(data):
    jolt_decimal = 0
    jolt_units = 0
    banks_joltage = []
    total_joltage = []
    for bank in data:
        jolt_decimal = max(int(x) for x in list(bank[:-1]))
        cut = list(bank).index(str(jolt_decimal))
        second_half = list(bank[cut + 1 :])

        jolt_units = max(second_half)
        joltage = int(str(jolt_decimal) + str(jolt_units))
        banks_joltage.append(joltage)
    total_joltage = sum(banks_joltage)
    return total_joltage


print("Part one solution is:", part_01(banks))


# Part two logic
def part_02(data):
    max_index = 0
    all_batteries = []
    single_battery = 0
    joltage_sum = 0

    for bank in data:
        left_index = 0
        right_index = 89
        scope = []
        single_battery = 0
        battery = []
        while right_index < 101:
            # setting the scope
            scope = bank[left_index:right_index]
            # finding index of the highest number
            max_index = scope.index(max(scope)) + left_index
            # appending value to a list
            battery.append(int(bank[max_index]))
            # moving the scope
            left_index = max_index + 1
            right_index += 1

        # creating joined numbers
        single_battery = int("".join(map(str, battery)))
        # appending
        all_batteries.append(single_battery)
        # calculating sum
        joltage_sum = sum(all_batteries)

    return joltage_sum


print("Part two solution is:", part_02(banks))
