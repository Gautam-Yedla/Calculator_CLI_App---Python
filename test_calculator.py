import unittest
from calculator import add, subtract, multiply, divide, exponent, modulus

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(subtract(10, 5), 5)

    def test_multiply(self):
        self.assertEqual(multiply(3, 4), 12)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(5, 0), "Error! Cannot divide by zero.")

    def test_exponent(self):
        self.assertEqual(exponent(2, 3), 8)

    def test_modulus(self):
        self.assertEqual(modulus(10, 3), 1)
        self.assertEqual(modulus(10, 0), "Error! Cannot mod by zero.")

if __name__ == "__main__":
    unittest.main()
