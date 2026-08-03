import unittest
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.logic.pattern_generator import generate_triangle, generate_inverted_triangle
from src.logic.matrix_calculator import generate_multiplication_table

class TestNestedLoopLogic(unittest.TestCase):

    def test_generate_triangle(self):
        expected = "*\n**\n***"
        self.assertEqual(generate_triangle(3), expected)

    def test_generate_inverted_triangle(self):
        expected = "***\n**\n*"
        self.assertEqual(generate_inverted_triangle(3), expected)

    def test_generate_multiplication_table(self):
        result = generate_multiplication_table(2)
        expected = [[1, 2], [2, 4]]
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()