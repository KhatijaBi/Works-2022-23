import unittest
from importlib import import_module

# Dynamically import Calculator class from Calculator.py
calculator_module = import_module("Calculator")
Calculator = getattr(calculator_module, "Calculator")

class CalculatorTests(unittest.TestCase):
    def test_add_1(self):
        calc = Calculator()
        self.assertEqual(10, calc.add(7, 3))

    def test_subtract_1(self):
        calc = Calculator()
        self.assertEqual(12, calc.subtract(15, 3))

    def test_multiply_1(self):
        calc = Calculator()
        self.assertEqual(34, calc.multiply(17,2))

    def test_SquareRoot(self):
        calc=Calculator()
        self.assertEqual(9,calc.squareRoot(81))
      
if __name__ == '__main__':
    unittest.main()