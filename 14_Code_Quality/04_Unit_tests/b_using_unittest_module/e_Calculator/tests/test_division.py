"""
Purpose: Testing division functionality in calculator
"""
import sys
import unittest

sys.path.insert(0, "..")
from calculator import division


class TestSuitedivision(unittest.TestCase):
    def test01(self):
        self.assertEqual(division(10, 20), 0.5)

    def test02(self):
        self.assertEqual(division(10, 20.0), 0.5)
        self.assertEqual(division(10.0, 20), 0.5)
        self.assertEqual(division(10.0, 20.0), 0.5)

    def test03(self):
        self.assertEqual(division(10.0, "20"), 0.5)
        self.assertEqual(division("10", "20"), 0.5)

        self.assertEqual(division("10.0", 20), 0.5)
        self.assertEqual(division("10.0", "20.0"), 0.5)

    @unittest.expectedFailure
    def test04(self):
        self.assertEqual(division("10.0", True), 0.5)
