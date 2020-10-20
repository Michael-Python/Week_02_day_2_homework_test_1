import unittest
# typo divide is repeated
from src.calculator import add, divide, multiply, subtract

class TestCalculator(unittest.TestCase):
    
    def test_add(self):
        # Calling add is the act part of the three As.
        # the 5 and the (2, 3) are the assert part.
        self.assertEqual(5, add(2, 3))
        # or
        # expected = 5
        # actual = add(2, 3)
        # self.assertEqual(expected, actual)

    def test_divide(self):
        self.assertEqual(5, divide(5, 1))

    def test_multiply(self):
        self.assertEqual(5, multiply(5, 1))

    def test_subtract(self):
        self.assertEqual(5, subtract(7, 2))