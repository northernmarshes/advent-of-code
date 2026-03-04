import numpy as np
from scipy.spatial import distance

input_file = "input.txt"
sample_file = "sample.txt"


def parse_data(data: str) -> np.ndarray:
    """Parsing the data"""
    box_coordinates = []
    box_coordinates_np = np.zeros
    with open(data, "r") as file:
        for layer in file.readlines():
            box_coordinates.append(list(map(int, layer[:-1].split(","))))
        box_coordinates_np = np.array(box_coordinates)
        return box_coordinates_np


def part_1(data: np.ndarray):
    """Part 1 logic"""

    d = distance.squareform(distance.pdist(data))
    closest = np.argsort(d, axis=1)
    closest_pairs = closest[:, 0:2]
    closest_pairs_distances = []

    for pair in closest_pairs:
        p1 = data[pair[0]]
        p2 = data[pair[1]]
        dist = np.linalg.norm(p1 - p2)
        closest_pairs_distances.append(float(dist))
    the_closest_pair = closest_pairs[
        closest_pairs_distances.index(min(closest_pairs_distances))
    ]

    return the_closest_pair


print(part_1(parse_data(sample_file)))
