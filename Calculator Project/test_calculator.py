# test_calculator.py

import unittest
from calculator import Calculator


class TestCalculator(unittest.TestCase):
    def setUp(self):
        """
        Create a new Calculator instance for each test.
        """
        self.calculator = Calculator()

    def test_add(self):
        self.assertEqual(self.calculator.add(5), 5)
        self.assertEqual(self.calculator.add(3), 8)

    def test_subtract(self):
        self.calculator.add(10)
        self.assertEqual(self.calculator.subtract(4), 6)
        self.assertEqual(self.calculator.subtract(2), 4)

    def test_multiply(self):
        self.calculator.add(2)
        self.assertEqual(self.calculator.multiply(5), 10)
        self.assertEqual(self.calculator.multiply(3), 30)

    def test_divide(self):
        self.calculator.add(20)
        self.assertEqual(self.calculator.divide(4), 5)
        with self.assertRaises(ValueError):
            self.calculator.divide(0)

    def test_take_root(self):
        self.calculator.add(27)
        self.assertEqual(self.calculator.take_root(3), 3)
        with self.assertRaises(ValueError):
            self.calculator.take_root(0)

    def test_reset_memory(self):
        self.calculator.add(10)
        self.calculator.reset_memory()
        self.assertEqual(self.calculator.memory, 0)


if __name__ == '__main__':
    unittest.main()
