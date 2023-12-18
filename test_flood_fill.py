import os
import unittest
from flood_fill import flood_fill, read_input, write_output

class TestFloodFill(unittest.TestCase):
    def setUp(self):
        print(f"\n\nRunning test: {self._testMethodName}")
        self.matrix = [['Y', 'Y', 'Y', 'G', 'G', 'G', 'G', 'G', 'G', 'G'],
                       ['Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'G', 'X', 'X', 'X'],
                       ['G', 'G', 'G', 'G', 'G', 'G', 'G', 'X', 'X', 'X'],
                       ['W', 'W', 'W', 'W', 'W', 'G', 'G', 'G', 'G', 'X'],
                       ['W', 'R', 'R', 'R', 'R', 'R', 'G', 'X', 'X', 'X'],
                       ['W', 'W', 'W', 'R', 'R', 'G', 'G', 'X', 'X', 'X'],
                       ['W', 'B', 'W', 'R', 'R', 'R', 'R', 'R', 'R', 'X'],
                       ['W', 'B', 'B', 'B', 'B', 'R', 'R', 'X', 'X', 'X'],
                       ['W', 'B', 'B', 'X', 'B', 'B', 'B', 'B', 'X', 'X'],
                       ['W', 'B', 'B', 'X', 'X', 'X', 'X', 'X', 'X', 'X']]

        self.expected_output = [['Y', 'Y', 'Y', 'G', 'G', 'G', 'G', 'G', 'G', 'G'],
                                ['Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'G', 'C', 'C', 'C'],
                                ['G', 'G', 'G', 'G', 'G', 'G', 'G', 'C', 'C', 'C'],
                                ['W', 'W', 'W', 'W', 'W', 'G', 'G', 'G', 'G', 'C'],
                                ['W', 'R', 'R', 'R', 'R', 'R', 'G', 'C', 'C', 'C'],
                                ['W', 'W', 'W', 'R', 'R', 'G', 'G', 'C', 'C', 'C'],
                                ['W', 'B', 'W', 'R', 'R', 'R', 'R', 'R', 'R', 'C'],
                                ['W', 'B', 'B', 'B', 'B', 'R', 'R', 'C', 'C', 'C'],
                                ['W', 'B', 'B', 'C', 'B', 'B', 'B', 'B', 'C', 'C'],
                                ['W', 'B', 'B', 'C', 'C', 'C', 'C', 'C', 'C', 'C']]

    def test_flood_fill(self):
        # Initialization of necessary data
        height, width = 10, 10
        start = (3, 9)
        target_color, replace_color = 'X', 'C'
        # Execution of filling
        flood_fill(self.matrix, start, replace_color, height, width)
        # Checking the result
        self.assertEqual(self.matrix, self.expected_output)

    def tearDown(self):
        print(f"Finish test: {self._testMethodName}\nResult: ", end="")

class TestInputOutput(unittest.TestCase):
    def setUp(self):
        print(f"\n\nRunning test: {self._testMethodName}")
        self.expected_read = (10, 10, (3, 9), 'C', [['Y', 'Y', 'Y', 'G', 'G', 'G', 'G', 'G', 'G', 'G'],
                                               ['Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'G', 'X', 'X', 'X'],
                                               ['G', 'G', 'G', 'G', 'G', 'G', 'G', 'X', 'X', 'X'],
                                               ['W', 'W', 'W', 'W', 'W', 'G', 'G', 'G', 'G', 'X'],
                                               ['W', 'R', 'R', 'R', 'R', 'R', 'G', 'X', 'X', 'X'],
                                               ['W', 'W', 'W', 'R', 'R', 'G', 'G', 'X', 'X', 'X'],
                                               ['W', 'B', 'W', 'R', 'R', 'R', 'R', 'R', 'R', 'X'],
                                               ['W', 'B', 'B', 'B', 'B', 'R', 'R', 'X', 'X', 'X'],
                                               ['W', 'B', 'B', 'X', 'B', 'B', 'B', 'B', 'X', 'X'],
                                               ['W', 'B', 'B', 'X', 'X', 'X', 'X', 'X', 'X', 'X']])

        self.expected_output = ("['Y', 'Y', 'Y', 'G', 'G', 'G', 'G', 'G', 'G', 'G']\n"
                                "['Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'G', 'X', 'X', 'X']\n"
                                "['G', 'G', 'G', 'G', 'G', 'G', 'G', 'X', 'X', 'X']\n"
                                "['W', 'W', 'W', 'W', 'W', 'G', 'G', 'G', 'G', 'X']\n"
                                "['W', 'R', 'R', 'R', 'R', 'R', 'G', 'X', 'X', 'X']\n"
                                "['W', 'W', 'W', 'R', 'R', 'G', 'G', 'X', 'X', 'X']\n"
                                "['W', 'B', 'W', 'R', 'R', 'R', 'R', 'R', 'R', 'X']\n"
                                "['W', 'B', 'B', 'B', 'B', 'R', 'R', 'X', 'X', 'X']\n"
                                "['W', 'B', 'B', 'X', 'B', 'B', 'B', 'B', 'X', 'X']\n"
                                "['W', 'B', 'B', 'X', 'X', 'X', 'X', 'X', 'X', 'X']\n")
        self.matrix = [['Y', 'Y', 'Y', 'G', 'G', 'G', 'G', 'G', 'G', 'G'],
                       ['Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'G', 'X', 'X', 'X'],
                       ['G', 'G', 'G', 'G', 'G', 'G', 'G', 'X', 'X', 'X'],
                       ['W', 'W', 'W', 'W', 'W', 'G', 'G', 'G', 'G', 'X'],
                       ['W', 'R', 'R', 'R', 'R', 'R', 'G', 'X', 'X', 'X'],
                       ['W', 'W', 'W', 'R', 'R', 'G', 'G', 'X', 'X', 'X'],
                       ['W', 'B', 'W', 'R', 'R', 'R', 'R', 'R', 'R', 'X'],
                       ['W', 'B', 'B', 'B', 'B', 'R', 'R', 'X', 'X', 'X'],
                       ['W', 'B', 'B', 'X', 'B', 'B', 'B', 'B', 'X', 'X'],
                       ['W', 'B', 'B', 'X', 'X', 'X', 'X', 'X', 'X', 'X']]

    def test_read_input(self):
        self.assertEqual(read_input('input.txt'), self.expected_read)

    def test_write_output(self):
        write_output('output_test.txt', self.matrix)
        with open('output_test.txt', 'r') as f:
            output = f.read()
        self.assertEqual(output, self.expected_output)

    def tearDown(self):
        if os.path.exists("output_test.txt"):
            os.remove("output_test.txt")
        print(f"Finish test: {self._testMethodName}\nResult: ", end="")

if __name__ == '__main__':
    unittest.main()
