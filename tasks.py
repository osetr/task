from operator import mul
from functools import reduce
from copy import deepcopy
from math import inf
import numpy as np


def fact(n: int) -> int:
    return reduce(mul, range(1, n + 1))


def digits_sum(number: int) -> int:
    factorial = fact(number)
    return reduce(lambda a, b: int(a) + int(b), str(factorial))


def number_of_true_brackets(N: int) -> int:
    return int(1 / (N + 1) * (fact(2 * N) / fact(N) ** 2))


class Dijkstra:
    def __init__(self, cities, cost_matrix, city_to_start_with):
        self.cities = cities
        self.cost_matrix = np.array(cost_matrix)
        self.city_to_start_with = city_to_start_with
        self.distances = {}

    def __repr__(self):
        return (
            "\ncities: "
            + str(self.cities)
            + "\ncost matrix:\n"
            + str(self.cost_matrix)
            + "\ncity to start with: "
            + str(self.city_to_start_with)
            + "\ndistances: "
            + str(self.distances)
        )

    def change_start_city(self, new_city_to_start_with):
        self.city_to_start_with = new_city_to_start_with

    def fit(self):
        index_start_city = self.cities.index(self.city_to_start_with)

        first_col = deepcopy(self.cost_matrix[:, 0])
        start_col = deepcopy(self.cost_matrix[:, index_start_city])
        self.cost_matrix[:, 0], self.cost_matrix[:, index_start_city] = (
            start_col,
            first_col,
        )

        first_row = deepcopy(self.cost_matrix[0, :])
        start_row = deepcopy(self.cost_matrix[index_start_city, :])
        self.cost_matrix[0, :], self.cost_matrix[index_start_city, :] = (
            start_row,
            first_row,
        )

        self.cities.remove(self.city_to_start_with)
        self.cities.insert(0, self.city_to_start_with)

        for i in range(len(self.cities)):
            distance = 0 if i == 0 else inf
            self.distances.update({self.cities[i]: distance})

        for city in self.distances:
            for i in range(len(self.cities)):
                if (
                    self.distances[city] + self.cost_matrix[self.cities.index(city), i]
                    < list(self.distances.values())[i]
                ):
                    self.distances.update(
                        {
                            list(self.distances.keys())[i]: self.distances[city]
                            + self.cost_matrix[self.cities.index(city), i]
                        }
                    )

    def distance_to_city(self, finish_city):
        return self.distances[finish_city]
