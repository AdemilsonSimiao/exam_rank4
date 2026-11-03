import unittest
from py_constellation_mapper import constellation_mapper

class TestConstellationMapper(unittest.TestCase):
    def test_cases_constallation(self):
        self.assertEqual(constellation_mapper([(0, 0), (1, 1), (2, 2)], 3), ['*..', '.*.', '..*'])
        self.assertEqual(constellation_mapper([(1, 1), (0, 1), (2, 1), (1, 0), (1, 2)], 3), ['.*.', '***', '.*.'])
        self.assertEqual(constellation_mapper([], 2), ['..', '..'])
        self.assertEqual(constellation_mapper([(0, 0), (0, 0), (1, 1)], 2), ['*.', '.*'])
        self.assertEqual(constellation_mapper([(0, 0), (5, 5)], 3), ['*..', '...', '...'])
        self.assertEqual(constellation_mapper([(1, 0), (1, 1), (1, 2)], 3), ['...', '***', '...'])
        