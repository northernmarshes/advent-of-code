import numpy as np

input_file = "input.txt"
sample_file = "sample.txt"


def parse_data(data: str):
    # space = np.zeros((1000, 1000, 1000))
    box_coordinates = []
    box_coordinates_np = np.zeros
    with open(data, "r") as file:
        for layer in file.readlines():
            box_coordinates.append(list(layer[:-1].split(",")))
            box_coordinates_np = np.array(box_coordinates)
        return box_coordinates_np


print(parse_data(sample_file))


def part_1(data):
    pass
