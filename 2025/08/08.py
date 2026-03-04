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


def part_1(data: np.ndarray, connections: int):
    """Part 1 logic"""

    coordinates = data
    performed_connections = 0
    the_closest_pair = np.zeros

    # Calculating distances between boxes
    d = distance.squareform(distance.pdist(coordinates))
    closest = np.argsort(d, axis=1)
    print(closest)

    while performed_connections < connections:
        # Choosing closest pairs
        closest_pairs = closest[:, 0:2]
        closest_pairs_distances = []

        # Calculating which pair is the closest one
        for pair in closest_pairs:
            p1 = coordinates[pair[0]]
            p2 = coordinates[pair[1]]
            dist = np.linalg.norm(p1 - p2)
            closest_pairs_distances.append(float(dist))
            the_closest_pair = closest_pairs[
                closest_pairs_distances.index(min(closest_pairs_distances))
            ]

        # Deleting connecion from closest
        print(
            "tu usuwamy",
            closest[closest_pairs_distances.index(min(closest_pairs_distances))],
        )

        print("the closest pair is:", the_closest_pair)

        # print(
        #     np.delete(
        #         closest, (closest_pairs_distances.index(min(closest_pairs_distances)))
        #     )
        # )

        performed_connections += 1

    return the_closest_pair


print(part_1(parse_data(sample_file), number_of_connections))
