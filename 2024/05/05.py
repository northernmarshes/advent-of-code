sample_file = "sample.txt"
input_file = "input.txt"

data_cache = []


def parse_data(data: str):
    """Parsing the data"""
    if data not in data_cache:
        with open(data, "r") as f:
            rules = []
            updates = []
            lines = f.readlines()
            for line in lines:
                if "|" not in line:
                    updates.append((line[:-1]).split(","))
                else:
                    rules.append((line[:-1]).split("|"))
        data_cache.append(rules)
        data_cache.append(updates[1:])
    return data_cache


def part_01(data: str):
    """Part 1 logic"""
    rules = (parse_data(data))[0]
    updates = (parse_data(data))[1]
    updates_int = []
    rules_int = []
    ordered = False
    goodupdated = 0
    middle = 0

    for rule in rules:
        rule_int = [int(item) for item in rule]
        rules_int.append(rule_int)

    for update in updates:
        update_int = [int(item) for item in update]
        updates_int.append(update_int)

    for update in updates_int:
        ordered = True
        middleIndex = round((len(update) - 1) / 2)
        middle = update[middleIndex]
        for rule in rules_int:
            if set(rule).issubset(set(update)):
                index = update.index(rule[1])
                if rule[0] in update[index:]:
                    ordered = False
        if ordered:
            goodupdated += middle
    return goodupdated


print(
    part_01(input_file),
    "is what you get if you add up the middle page number from the correctly-ordered updates",
)
