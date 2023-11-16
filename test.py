from main import find_unreachable
import unittest

class TestIsConnected(unittest.TestCase):

    def test_connected_case(self):
        """
        S_0
         ↓
        C_0 → C_1 → C_2
        !↓
        S_1
        """
        cities = ['City_0', 'City_1', 'City_2']
        storages = ['Storage_0', 'Storage_1']
        pipelines = [['City_0', 'City_1'], ['City_1', 'City_2'], ['Storage_0', 'City_0'], ['Storage_1', 'City_0']]
        result = find_unreachable(cities, storages, pipelines)
        expected = []
        self.assertEqual(result, expected)

    def test_disconnected_case(self):
        """
        S_0
         ↓
        C_0 → C_1 → C_2
              !↓
              S_1
        """
        cities = ['City_0', 'City_1', 'City_2']
        storages = ['Storage_0', 'Storage_1']
        pipelines = [['City_0', 'City_1'], ['City_1', 'City_2'], ['Storage_0', 'City_0'], ['Storage_1', 'City_1']]
        result = find_unreachable(cities, storages, pipelines)
        expected = [['Storage_1', ['City_0']]]
        self.assertEqual(result, expected)

    def test_given_situation(self):
        """
        C_1 → C_2

        Dolyna → Lviv → Stryy
        """
        cities = ['Львів', 'Стрий', 'Долина']
        storages = ['Сховище_1', 'Сховище_2']
        pipelines = [['Львів', 'Стрий'], ['Долина', 'Львів'], ['Сховище_1', 'Сховище_2']]
        result = find_unreachable(cities, storages, pipelines)
        expected = [['Сховище_1', ['Львів', 'Стрий', 'Долина']], ['Сховище_2', ['Львів', 'Стрий', 'Долина']]]
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
