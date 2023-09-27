import unittest
from module.length_peak_sequence import length_peak_sequence


class TestLongestPeak(unittest.TestCase):
    def test_sorted_ascending(self):
        self.assertEqual(length_peak_sequence([1, 2, 3, 4, 5]), 0)

    def test_sorted_descending(self):
        self.assertEqual(length_peak_sequence([5, 4, 3, 2, 1]), 0)

    def test_two_elements(self):
        self.assertEqual(length_peak_sequence([1, 2]), 0)

    def test_no_peaks(self):
        self.assertEqual(length_peak_sequence([3, 2, 1, 2, 3]), 0)

    def test_multiple_peaks(self):
        self.assertEqual(length_peak_sequence([1, 3, 5, 4, 2, 8, 3, 7, 2, 0]), 5)

    def test_not_symmetrical_peak(self):
        self.assertEqual(length_peak_sequence([1, 3, 5, 7, 4, 2, 9, 8]), 6)
        self.assertEqual(length_peak_sequence([8, 9, 2, 4, 7, 5, 3, 1]), 6)

if __name__ == '__main__':
    unittest.main()