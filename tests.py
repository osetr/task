import unittest
from math import inf
from tasks import digits_sum, number_of_true_brackets, Dijkstra


class TestSumOfFactDigits(unittest.TestCase):
    def test_number_100(self):
        self.assertEqual(digits_sum(100), 648)


class CheapestTravel(unittest.TestCase):
    def test_first_case(self):
        dij = Dijkstra(
            ["gdansk", "bydgoszcz", "torun", "warszawa"],
            [[0, 1, 3, inf],
             [1, 0, 1, 4],
             [3, 1, 0, 1],
             [inf, 4, 1, 0]],
        )

        dij.fit()
        self.assertEqual(dij.distance_to_city("warszawa"), 3)

    def test_second_case(self):
        dij = Dijkstra(
            ["gdansk", "bydgoszcz", "torun", "warszawa"],
            [[0, 1, 3, inf],
             [1, 0, 1, 4],
             [3, 1, 0, 1],
             [inf, 4, 1, 0]],
        )

        dij.change_start_city('bydgoszcz')
        dij.fit()
        self.assertEqual(dij.distance_to_city("warszawa"), 2)


class NumerOfTrueBrackets(unittest.TestCase):
    def test_N_1(self):
        self.assertEqual(number_of_true_brackets(1), 1)

    def test_N_2(self):
        self.assertEqual(number_of_true_brackets(2), 2)

    def test_N_3(self):
        self.assertEqual(number_of_true_brackets(3), 5)

    def test_N_4(self):
        self.assertEqual(number_of_true_brackets(4), 14)

    def test_N_7(self):
        self.assertEqual(number_of_true_brackets(7), 429)


if __name__ == "__main__":
    unittest.main()
