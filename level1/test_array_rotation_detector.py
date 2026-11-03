import unittest
from py_array_rotation_detector import array_rotation_detector

class TestPyArrayRotationDetector(unittest.TestCase):
    def test_true_validatiopn(self):
        self.assertTrue("ok", array_rotation_detector([1, 2, 3, 4, 5], [4, 5, 1, 2, 3]))
        self.assertTrue("ok", array_rotation_detector([1, 2, 3, 4, 5], [5, 1, 2, 3, 4]))
        self.assertTrue("ok", array_rotation_detector([], []))
    
    def test_false_validatiopn(self):
        self.assertFalse(array_rotation_detector([1, 2, 3], [3, 2, 1]))
        self.assertFalse(array_rotation_detector([1, 2], [1, 2, 3]))
