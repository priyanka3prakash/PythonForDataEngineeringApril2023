from unittest import TestCase

from myscript import Calculator


class TestCalculator(TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_summation(self):
        answer = self.calc.summation(2, 4)
        self.assertEqual(answer, 6)
