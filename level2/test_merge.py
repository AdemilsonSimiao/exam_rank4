import unittest
from py_merge_sorted_lists import merge_sorted_lists

class TestMerge(unittest.TestCase):
    def test(self):
        self.assertEqual(merge_sorted_lists([[1, 3, 5], [2, 4, 6]]), [1, 2, 3, 4, 5, 6])
        self.assertEqual(merge_sorted_lists([[1, 5, 9], [2, 3, 8], [4, 6, 7]]), [1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.assertEqual(merge_sorted_lists([[5], [1, 3], [2, 4]]), [1, 2, 3, 4, 5])
        self.assertEqual(merge_sorted_lists([[1, 1, 2], [2, 3, 3]]), [1, 1, 2, 2, 3, 3])
        self.assertEqual(merge_sorted_lists([[], [1, 2, 3]]), [1, 2, 3])
        self.assertEqual(merge_sorted_lists([[]]), [])
        self.assertEqual(merge_sorted_lists([[-5, -1, 0], [-3, 2, 4]]), [-5, -3, -1, 0, 2, 4])
        self.assertEqual(merge_sorted_lists([[10], [10], [10]]), [10, 10, 10])
