# Input files
input_file = "input.txt"
sample_file = "sample.txt"

# Variables
left_list = []
right_list = []

# File loading
with open(input_file, "r") as f:
    lines = f.readlines()
    for line in lines:
        if "  " in line:
            left_list.append(int(line.split("  ")[0]))
            right_list.append(int((line.split("  ")[1])[:-1]))


def part_01(list_one, list_two):
    # Sorting
    list_one = sorted(list_one)
    list_two = sorted(list_two)

    distances = []
    pair = []
    for num in range(len(list_one)):
        pair.append(list_one[num])
        pair.append(list_two[num])
        pair = sorted(pair)
        distances.append(pair[1] - pair[0])
        pair = []
    sum_of_distances = sum(distances)
    return sum_of_distances


print(part_01(left_list, right_list), "is the total distance between the lists.")


def part_02(list_one, list_two):
    similarity_total = []
    for num in list_one:
        appearances = list_two.count(num)
        similarity_score = num * appearances
        similarity_total.append(similarity_score)

    similarity_int = list(map(int, similarity_total))
    similarity_sum = sum(similarity_int)
    return similarity_sum


print(part_02(left_list, right_list), "Is the similarity score of the two lists.")
