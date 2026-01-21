sample_file = "sample.txt"
input_file = "input.txt"

data_cache = []


def parse_data(data: str):
    """Parsing the data"""
    if data not in data_cache:
        with open(sample_file, "r") as f:
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
    page_order = []
    rules = (parse_data(data))[0]
    updates = (parse_data(data))[1]


part_01(sample_file)
