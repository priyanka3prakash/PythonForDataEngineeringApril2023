"""
Purpose: Testing addition functionality in calculator
"""
import sys
import unittest

# import os 
# print(os.listdir('..'))

sys.path.insert(0, "..")
from calculator import addition

# for each_path in sys.path:
#     print(each_path)



class TestSuiteAddition(unittest.TestCase):
    def test01(self):
        self.assertEqual(addition(10, 20), 30)

    def test02(self):
        self.assertEqual(addition(10, 20.0), 30.0)
        self.assertEqual(addition(10.0, 20), 30.0)
        self.assertEqual(addition(10.0, 20.0), 30.0)

    def test03(self):
        self.assertEqual(addition(10.0, "20"), 30.0)
        self.assertEqual(addition("10", "20"), 30.0)

        self.assertEqual(addition("10.0", 20), 30.0)
        self.assertEqual(addition("10.0", "20.0"), 30.0)

    @unittest.expectedFailure
    def test04(self):
        self.assertEqual(addition("10.0", True), 30.0)
