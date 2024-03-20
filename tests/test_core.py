# tests/test_core.py

# To execute de test, use the following command: python -m unittest discover tests

import unittest
from calculator.core import (
    add, subtraction, multiplication, division,
    power, square_root, logarithm, evaluate_expression
)

class TestCore(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_subtraction(self):
        self.assertEqual(subtraction(5, 3), 2)

    def test_multiplication(self):
        self.assertEqual(multiplication(2, 3), 6)

    def test_division(self):
        self.assertEqual(division(6, 3), 2)
        with self.assertRaises(ValueError):
            division(5, 0)

    def test_power(self):
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(4, 0.5), 2)

    def test_square_root(self):
        self.assertEqual(square_root(4), 2)
        self.assertEqual(square_root(16), 4)
        self.assertRaises(ValueError, square_root, -1)

    def test_logarithm(self):
        self.assertAlmostEqual(logarithm(1), 0)
        self.assertAlmostEqual(logarithm(10, 10), 1)
        self.assertRaises(ValueError, logarithm, -1)

    def test_evaluate_expression(self):
        # Suponiendo que evaluate_expression devuelve un objeto sympy y usas .evalf() para obtener un número flotante
        self.assertAlmostEqual(evaluate_expression("2 + 3").evalf(), 5)
        self.assertAlmostEqual(evaluate_expression("2 * (3 + 4)").evalf(), 14)
        self.assertAlmostEqual(evaluate_expression("sqrt(16)").evalf(), 4)


if __name__ == '__main__':
    unittest.main()