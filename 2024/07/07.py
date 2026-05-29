import pytest

data_cache = {}


def main():
    input = "input.txt"
    print(
        f"The sum of the test values for the three equations listed above is {part_01(input)}"
    )
    pass


def part_01(input: str):
    pass


def parse(data: str):
    """Parsing the data"""
    if data not in data_cache:
        with open(data, "r") as f:
            # numbers = []
            lines = f.readlines()
            for line in lines:
                pass

    return data_cache[data]


if __name__ == "__main__":
    main()


@pytest.fixture
def sample_data():
    sample = """190: 10 19
    3267: 81 40 27
    83: 17 5
    156: 15 6
    7290: 6 8 6 15
    161011: 16 10 13
    192: 17 8 14
    21037: 9 7 18 13
    292: 11 6 16 20"""
    return sample


def test_part_01(sample_data):
    assert part_01(sample_data) == 3749
