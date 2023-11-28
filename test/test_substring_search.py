import unittest
from src.substring_search import find_needle


class TestSubstringSearch(unittest.TestCase):
    def test_find_needle(self):
        haystack = "ababcababcabc"
        needle = "abc"
        self.assertEqual(find_needle(haystack, needle), [2, 7, 10])

    def test_find_needle_empty_needle(self):
        haystack = "ababcababcabc"
        needle = ""
        self.assertEqual(find_needle(haystack, needle), [])

    def test_find_needle_no_occurrences(self):
        haystack = "ababcababcabc"
        needle = "xyz"
        self.assertEqual(find_needle(haystack, needle), [])


if __name__ == "__main__":
    unittest.main()
