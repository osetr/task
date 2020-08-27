from operator import mul
from functools import reduce
from copy import deepcopy
from math import inf
import numpy as np


def fact(n: int) -> int:
    """
        Return n!
    """
    return reduce(mul, range(1, n + 1))


# Task 1
def number_of_true_brackets(N: int) -> int:
    """
        Return amount of balanced brackets expressions,
        which can be made of N brackets pairs.
        Actually return Nth element of Сatalan sequence.
    """
    return int(1 / (N + 1) * (fact(2 * N) / fact(N) ** 2))


# Task 2
class Dijkstra:
    """
        To get instance of this class, put into __init__
        parameters in following format:
            cities = ['city1', 'city2', 'city3', ...]
            cost_matrix = [[0, 3, inf],
                           [3, 0, 1],
                           [inf, 1, 0]]
        Cities is just a full list of cites.
        In cost matrix each element has index, appropriate to
        city position into cities list. (i,j)th element is a price
        of travel from i-th city to j-th or otherwise.
        Note that matrix has to be symmetric, and has zeros
        on the main diagonal.
        Аfter creating an instance, it will store start_city, which
        serves as a starting point for the distances to other cities.
        You can change it by change_start_city(new_start_city).
        After invoked fit(), you can get all distances to all cities,
        starting from start_city in distances, which format is:
        {'city1': 123.0, 'city2': 56.0, ...} or some special distance
        by distance_to_city(finish_city).
        So act in the following gradations:
        get instance -> change start if necessary -> fit -> get distance
    """

    def __init__(self, cities, cost_matrix):
        self.cities = cities
        self.cost_matrix = np.array(cost_matrix)
        self.start_city = self.cities[0]
        self.distances = {}

    def __repr__(self):
        return (
            "\ncities: "
            + str(self.cities)
            + "\ncost matrix:\n"
            + str(self.cost_matrix)
            + "\ncity to start with: "
            + str(self.start_city)
            + "\ndistances: "
            + str(self.distances)
        )

    def change_start_city(self, new_start_city):
        """
            Change start city.
        """
        self.start_city = new_start_city

    def fit(self):
        """
            This function is just implementation of Dijkstra's alghoritm.
            If you have your start city changed, fit() will replace
            elements in cost matrix and cities list, so that you will
            have conformity between them.
        """
        index_start_city = self.cities.index(self.start_city)
        cities_amount = len(self.cities)

        # replace columns in cost matrix
        first_col = deepcopy(self.cost_matrix[:, 0])
        start_col = deepcopy(self.cost_matrix[:, index_start_city])
        self.cost_matrix[:, 0], self.cost_matrix[:, index_start_city] = (
            start_col,
            first_col,
        )

        # replace rows in cost matrix
        first_row = deepcopy(self.cost_matrix[0, :])
        start_row = deepcopy(self.cost_matrix[index_start_city, :])
        self.cost_matrix[0, :], self.cost_matrix[index_start_city, :] = (
            start_row,
            first_row,
        )

        # put new start city on the first place in cities list
        self.cities.remove(self.start_city)
        self.cities.insert(0, self.start_city)

        # start of Dijkstra's alghoritm
        # first get distances like {'city1':0,'city2': inf,'city3': inf, ...}
        for i in range(cities_amount):
            distance = 0 if i == 0 else inf
            self.distances.update({self.cities[i]: distance})

        # now lets move through all prices and take better of them
        for city in self.distances:
            for i in range(cities_amount):

                current_city_weight = self.distances[city]
                goal_city_price = self.cost_matrix[self.cities.index(city), i]
                goal_city_name = list(self.distances.keys())[i]
                goal_city_weight = list(self.distances.values())[i]

                if current_city_weight + goal_city_price < goal_city_weight:
                    self.distances.update(
                        {goal_city_name: current_city_weight + goal_city_price}
                    )

    def distance_to_city(self, finish_city):
        """
            Return distance from start city to finish city
        """
        return self.distances[finish_city]


# Task 3
def digits_sum(number: int) -> int:
    """
        Takes some number and return sum of digits
         of this number's factorial
    """
    factorial = fact(number)
    return reduce(lambda a, b: int(a) + int(b), str(factorial))
