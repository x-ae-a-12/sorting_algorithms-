"""
tests...
"""

import unittest
import numpy as np
from algorithms.main import Sorter


class SorterCheck(unittest.TestCase):
    """
    Some tests to check quicker simple sorting algorithm...
    """
    def test_ideal_case(self):
        sorter = Sorter()
        array = [3, 9, 1, 10, 6, 8, 4, 7, 2, 5]
        self.assertEqual(sorter.simple_1v1_quicker_model(array), sorted(array))

    def test_ideal_case_long_distance(self):
        sorter = Sorter()
        array = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        self.assertEqual(sorter.simple_1v1_quicker_model(array), sorted(array))

    def test_ideal_case_float(self):
        sorter = Sorter()
        array = np.random.sample(10)
        ans = np.array_equal(sorter.simple_1v1_quicker_model(array), sorted(array))
        self.assertEqual(ans, True)


if __name__ == '__main__':
    unittest.main()
