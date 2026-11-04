import unittest
from py_list_intersection_finder import list_intersection_finder

class TestListIntersectionFinder(unittest.TestCase):
    def test_intersection_finder(self):
        self.assertEqual(list_intersection_finder([[1, 2, 3], [2, 3, 4], [2, 3, 5]]), [2, 3])
        self.assertEqual(list_intersection_finder([[1, 2, 3, 4], [2, 4, 6, 8], [4, 8, 12]]), [4])
        self.assertEqual(list_intersection_finder([[1, 1, 2, 3], [1, 2, 2, 3], [1, 2, 3, 3]]), [1, 2, 3])
        self.assertEqual(list_intersection_finder([[5]]), [5])
        
    def test_empty_cases(self):
        self.assertEqual(list_intersection_finder([[1, 2, 3], [4, 5, 6]]), [])
        self.assertEqual(list_intersection_finder([]), [])
        self.assertEqual(list_intersection_finder([[1, 2, 3], []]), [])
