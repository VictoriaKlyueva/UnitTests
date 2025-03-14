import unittest

from Calculator import Calculator
from History import History


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.history = History()
        self.calculator = Calculator(self.history)

    def test_sum(self):
        self.assertEqual(self.calculator.sum(2, 3), 5)
        self.assertEqual(self.calculator.sum(-1, 1), 0)
        self.assertEqual(self.calculator.sum(0, 0), 0)

        self.assertEqual(self.history.data, [(2, 3, 5), (-1, 1, 0), (0, 0, 0)])


if __name__ == '__main__':
    unittest.main()
