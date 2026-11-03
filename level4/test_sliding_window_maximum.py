import unittest
from py_sliding_window_maximum import sliding_window_maximum

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sliding_window_maximum([1, 3, -1, -3, 5, 3, 6, 7], 3), [3, 3, 5, 5, 6, 7])
        self.assertEqual(sliding_window_maximum([1, 2, 3, 4, 5], 2), [2, 3, 4, 5])
        self.assertEqual(sliding_window_maximum([5, 4, 3, 2, 1], 1), [5, 4, 3, 2, 1])
        self.assertEqual(sliding_window_maximum([1, 2, 3], 3), [3])
        self.assertEqual(sliding_window_maximum([1, 2, 3], 4), [])
        self.assertEqual(sliding_window_maximum([], 2), [])
        self.assertEqual(sliding_window_maximum([1, 2, 3], 0), [])
