import unittest
from py_palindrome_partitioner import palindrome_partitioner

class TestPalindromePartitioner(unittest.TestCase):
    def test_palindrome_partitioner(self):
        self.assertEqual(palindrome_partitioner("aab"), 1)
        self.assertEqual(palindrome_partitioner("aba"), 0)
        self.assertEqual(palindrome_partitioner("abc"), 2)
