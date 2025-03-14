import unittest

from Calculator import Calculator
from History import History


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.history = History()
        self.calculator = Calculator(self.history)

    def test_sum_positive_numbers(self):
        self.assertEqual(self.calculator.sum(2, 3), 5)
        self.assertEqual(self.history.data[-1], (2, 3, 5))

    def test_sum_negative_numbers(self):
        self.assertEqual(self.calculator.sum(-5, -3), -8)
        self.assertEqual(self.history.data[-1], (-5, -3, -8))

    def test_sum_mixed_numbers(self):
        self.assertEqual(self.calculator.sum(10, -4), 6)
        self.assertEqual(self.history.data[-1], (10, -4, 6))

    def test_sum_zero(self):
        self.assertEqual(self.calculator.sum(0, 0), 0)
        self.assertEqual(self.history.data[-1], (0, 0, 0))

        self.assertEqual(self.calculator.sum(5, 0), 5)
        self.assertEqual(self.history.data[-1], (5, 0, 5))

    def test_sum_large_numbers(self):
        self.assertEqual(self.calculator.sum(123456789, 987654321), 1111111110)
        self.assertEqual(self.history.data[-1], (123456789, 987654321, 1111111110))

    def test_sum_float_numbers(self):
        self.assertAlmostEqual(self.calculator.sum(1.5, 2.5), 4.0)
        self.assertEqual(self.history.data[-1], (1.5, 2.5, 4.0))

    def test_sum_invalid_input(self):
        with self.assertRaises(ValueError):
            self.calculator.sum("2", 3)

        with self.assertRaises(ValueError):
            self.calculator.sum(2, "3")

        with self.assertRaises(ValueError):
            self.calculator.sum("a", "b")

    def test_history_storage(self):
        self.calculator.sum(1, 2)
        self.calculator.sum(3, 4)
        self.calculator.sum(5, 6)

        expected_history = [
            (1, 2, 3),
            (3, 4, 7),
            (5, 6, 11),
        ]
        self.assertEqual(self.history.data, expected_history)


if __name__ == '__main__':
    unittest.main()
