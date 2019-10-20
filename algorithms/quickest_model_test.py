"""
tests...
"""

import unittest
import numpy as np
from algorithms.main import Sorter


class SorterCheck(unittest.TestCase):
    """
    Some tests to check quickest sorting algorithm...
    """
    def test_ideal_case(self):
        sorter = Sorter()
        array = [7, 9, 5, 10, 6, 8, 4, 3, 2, 1]
        self.assertEqual(sorter._quickest_model(array), sorted(array))

    def test_ideal_case_long_distance(self):
        sorter = Sorter()
        array = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        self.assertEqual(sorter._quickest_model(array), sorted(array))

    def test_ideal_case_float(self):
        sorter = Sorter()
        array = np.random.sample(10)
        ans = np.array_equal(sorter._quickest_model(array), sorted(array))
        self.assertEqual(ans, True)

    def test_ideal_case_odd(self):
        sorter = Sorter()
        array = np.random.sample(11)
        ans = np.array_equal(sorter._quickest_model(array), sorted(array))
        self.assertEqual(ans, True)


if __name__ == '__main__':
    unittest.main()
