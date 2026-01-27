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
                if "|" not in line and "," in line:
                    line = (line[:-1]).split(",")
                    line = [int(item) for item in line]
                    updates.append(line)
                if "|" in line:
                    line = (line[:-1]).split("|")
                    line = [int(item) for item in line]
                    rules.append(line)
        data_cache.append(rules)
        data_cache.append(updates)
    return data_cache


def part_01(data: str):
    """Part 1 logic"""
    rules = (parse_data(data))[0]
    updates = (parse_data(data))[1]
    result = 0

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
    return result


print(
    part_01(input_file),
    "is what you get if you add up the middle page number from the correctly-ordered updates",
)
