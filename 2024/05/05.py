sample_file = "sample.txt"
input_file = "input.txt"

data_cache = {}


def parse_data(data: str):
    """Parsing the data"""
    if data not in data_cache:
        with open(data, "r") as f:
            rules = []
            updates = []
            lines = f.readlines()
            for line in lines:
                if "|" not in line and "," in line:
                    line = (line[:-1]).split(",")
                    line = [int(item) for item in line]
                    updates.append(line)
                elif "|" in line:
                    line = (line[:-1]).split("|")
                    line = [int(item) for item in line]
                    rules.append(line)
        data_cache[data] = (rules, updates)
    return data_cache[data]


def part_01(data: str):
    """Part 1 logic"""
    rules, updates = parse_data(data)
    output = []
    result = 0
    unordered = []

    for update in updates:
        ordered = True
        middle = update[(round((len(update) - 1) / 2))]
        for rule in rules:
            if set(rule).issubset(set(update)):
                index = update.index(rule[1])
                if rule[0] in update[index:]:
                    ordered = False
        if ordered:
            result += middle
        else:
            unordered.append(update)
    output.append(result)
    output.append(unordered)
    return output


print(
    part_01(sample_file)[0],
    "is what you get if you add up the middle page number from the correctly-ordered updates",
)


def part_02(data: str, unordered: list):
    """Part 2 logic"""
    rules = parse_data(data)[0]
    order = []
    order.append(rules[0][0])
    order.append(rules[0][1])
    for rule in rules:
        if rule[0] in order and rule[1] not in order:
            index = order.index(rule[0])
            order.insert(index + 1, rule[1])
        if rule[0] not in order and rule[1] in order:
            index = order.index(rule[1])
            order.insert(index - 1, rule[0])
    print(order)


part_02(sample_file, part_01(sample_file)[1])

# Sort list 'a' based on 'order'
# sorted_list = sorted(a, key=lambda x: order.index(x))
# print(sorted_list)
