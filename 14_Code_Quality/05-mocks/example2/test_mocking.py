from unittest import TestCase
from unittest.mock import patch


class TestCalculator(TestCase):
    @patch("myscript.Calculator.summation", return_value=9)
    def test_sum(self, _summation):
        self.assertEqual(_summation(2, 3), 9)
