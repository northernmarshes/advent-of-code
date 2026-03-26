import regex as re

input_file = "input.txt"
sample_file = "sample.txt"


def parse_data(data: str) -> list:
    """Parsing the data"""
    games = []
    with open(data, "r") as f:
        lines = f.readlines()
        for line in lines:
            game = {
                "number": None,
                "blue": None,
                "green": None,
                "red": None,
            }
            games.append(game)
    return games
