# tests/test_core.py

# To execute de test, use the following command: python -m unittest discover tests

import unittest
from calculator.core import add, subtraction, multiplication, divison

class TestCore(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_subtraction(self):
        self.assertEqual(subtraction(5, 3), 2)

    def test_multiplication(self):
        self.assertEqual(multiplication(2, 3), 6)

    def test_division(self):
        self.assertEqual(divison(6, 3), 2)
        with self.assertRaises(ValueError):
            divison(5, 0)


if __name__ == '__main__':
    unittest.main()