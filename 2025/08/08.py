import numpy as np
from scipy.spatial import distance
import itertools
import math

input_file = "input.txt"
sample_file = "sample.txt"
number_of_connections = 1000


def parse_data(data: str) -> np.ndarray:
    """Parsing the data"""
    box_coordinates = []
    box_coordinates_np = np.zeros
    with open(data, "r") as file:
        for layer in file.readlines():
            box_coordinates.append(list(map(int, layer[:-1].split(","))))
        box_coordinates_np = np.array(box_coordinates)
        return box_coordinates_np


def circuit_lenghts(pairs: list) -> int:
    """Calculating multiplication of 3 longest circuit lengths"""
    lengths = []
    boxes = set(map(frozenset, pairs))
    groups = []

    # Appending boxes into groups
    while boxes:
        group = set()
        groups.append([])
        while True:
            for candidate in boxes:
                if not group or group & candidate:
                    group |= candidate
                    groups[-1].append(list(candidate))
                    boxes.remove(candidate)
                    break
            else:
                break

    for group in groups:
        lengths.append(len(set(list(itertools.chain.from_iterable(group)))))

    # Multiplying three longest circuits
    result = math.prod(sorted(lengths)[-3:])

    return result


def part_1(data: np.ndarray, connections: int) -> int:
    """Part 1 logic"""
    coordinates = data
    performed_connections = 0
    the_closest_pair = np.zeros
    connected_boxes = []

    # Calculating distances between boxes
    d = distance.squareform(distance.pdist(coordinates))
    closest = list(np.argsort(d, axis=1))
    closest_list = []
    for row in closest:
        closest_list.append([int(char) for char in row])

    # Choosing closest pairs
    while performed_connections < connections:
        closest_pairs = [row[:2] for row in closest_list]
        closest_pairs_distances = []
        the_closest_pair = []

        # Calculating which pair is the closest one
        for pair in closest_pairs:
            p1 = coordinates[pair[0]]
            p2 = coordinates[pair[1]]
            dist = np.linalg.norm(p1 - p2)
            closest_pairs_distances.append(float(dist))
            the_closest_pair = closest_pairs[
                closest_pairs_distances.index(min(closest_pairs_distances))
            ]
        # Deleting used connections from a proximity list
        del closest_list[the_closest_pair[0]][1]
        del closest_list[the_closest_pair[1]][1]

        # Appending a new connction to a list
        connected_boxes.append(the_closest_pair)
        performed_connections += 1

    result = circuit_lenghts(connected_boxes)
    return result


print(
    part_1(parse_data(input_file), number_of_connections),
    "is the number of multiplied together the sizes of the three largest circuits.",
)
