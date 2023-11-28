import unittest
from src.knuth_morris_pratt import knuth_morris_pratt


class TestKnuthMorrisPratt(unittest.TestCase):
    def test_empty_needle(self):
        haystack = "abc"
        needle = ""
        result = knuth_morris_pratt(haystack, needle)
        self.assertEqual(result, [])

    def test_no_match(self):
        haystack = "abcde"
        needle = "xyz"
        result = knuth_morris_pratt(haystack, needle)
        self.assertEqual(result, [])

    def test_single_match(self):
        haystack = "abcde"
        needle = "cd"
        result = knuth_morris_pratt(haystack, needle)
        self.assertEqual(result, [2])

    def test_multiple_matches(self):
        haystack = "ababab"
        needle = "ab"
        result = knuth_morris_pratt(haystack, needle)
        self.assertEqual(result, [0, 2, 4])


if __name__ == "__main__":
    unittest.main()
