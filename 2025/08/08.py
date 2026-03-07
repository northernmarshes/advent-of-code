import numpy as np
from scipy.spatial import distance

input_file = "input.txt"
sample_file = "sample.txt"
number_of_connections = 10


def parse_data(data: str) -> np.ndarray:
    """Parsing the data"""
    box_coordinates = []
    box_coordinates_np = np.zeros
    with open(data, "r") as file:
        for layer in file.readlines():
            box_coordinates.append(list(map(int, layer[:-1].split(","))))
        box_coordinates_np = np.array(box_coordinates)
        return box_coordinates_np


test_pairs = [(0, 19), (0, 7), (2, 13), (7, 19)]


def connect_pairs(pairs: list) -> list:
    """Sorting pairs into connections"""

    groups = []
    if len(pairs) > 1:
        tmp = [pairs[0]]
        for i in range(1, len(pairs)):
            if (
                pairs[i][0] == pairs[i - 1][1]
                or pairs[i][1] == pairs[i - 1][0]
                or pairs[i][1] == pairs[i - 1][1]
                or pairs[i][0] == pairs[i - 1][0]
            ):
                tmp.append(pairs[i])
            else:
                groups.append(tmp)
                tmp = [pairs[i]]
        groups.append(tmp)
    else:
        groups = pairs

    for group in groups:
        print(group)

    return groups


def part_1(data: np.ndarray, connections: int):
    """Part 1 logic"""

    coordinates = data
    performed_connections = 0
    the_closest_pair = np.zeros
    connected_boxes = []
    # multiplied_sizes = 0

    # Calculating distances between boxes
    d = distance.squareform(distance.pdist(coordinates))
    closest = list(np.argsort(d, axis=1))
    closest_list = []
    for row in closest:
        closest_list.append([int(char) for char in row])

    while performed_connections < connections:
        # Choosing closest pairs
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

    return connected_boxes


# print(part_1(parse_data(sample_file), number_of_connections))

# print(connect_pairs(part_1(parse_data(sample_file), 10)))
print(connect_pairs(test_pairs))
