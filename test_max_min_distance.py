import unittest

from max_min_distance import can_place_cows, max_min_distance

class TestMaxMinDistance(unittest.TestCase):
    def test_example_case(self):
        N = 5
        C = 3
        free_sections = [1, 2, 8, 4, 9]
        result = max_min_distance(N, C, free_sections)
        self.assertEqual(result, 3)

    def test_custom_cases(self):
        # Додайте додаткові власні тести для перевірки
        N = 10
        C = 4
        free_sections = [1, 20, 6, 30, 12, 15, 3, 22, 25, 8]
        result = max_min_distance(N, C, free_sections)
        self.assertEqual(result, 8)

    def test_edge_cases(self):
        # Тести на межі можливого вхідного діапазону
        N = 2
        C = 2
        free_sections = [1, 1000000000]
        result = max_min_distance(N, C, free_sections)
        self.assertEqual(result, 999999999)

        N = 10
        C = 10
        free_sections = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        result = max_min_distance(N, C, free_sections)
        self.assertEqual(result, 1)

class TestCanPlaceCows(unittest.TestCase):
    def test_can_place_cows(self):
        mid = 3
        N = 5
        C = 3
        free_sections = [1, 2, 4, 8, 9]
        result = can_place_cows(mid, N, C, free_sections, [])
        self.assertTrue(result)

    def test_cannot_place_cows(self):
        mid = 4
        N = 5
        C = 3
        free_sections = [1, 2, 4, 8, 9]
        result = can_place_cows(mid, N, C, free_sections, [])
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
