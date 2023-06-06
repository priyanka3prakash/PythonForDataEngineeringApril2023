import unittest


def addition(n1, n2):
    return float(n1) + float(n2)
    # return int(n1) + int(n2)
    # return n1 + n2


class TestAddition(unittest.TestCase):
    def test01_addition_positive(self): # Happy testing
        print("In test case - test01_addition_positive")
        # assert addition(10, 20) == 30
        self.assertEqual(addition(10, 20), 30)
        self.assertEqual(addition(10, 20.0), 30.0)
        self.assertEqual(addition(10.0, 20), 30.0)
        self.assertEqual(addition(10.0, 20.0), 30.0)

    def test02_addition_positive_critical(self):
        print("In test case - test02_addition_positive_critical")
        self.assertEqual(addition(10.0, "20"), 30.0)
        self.assertEqual(addition("10.0", 20), 30.0)
        self.assertEqual(addition("10.0", "20"), 30.0)

    @unittest.skip("skipping for some reason")
    def test03_addition_positive(self):
        print("In test case - test03_addition_positive")
        # assert addition(10, 20) == 30
        self.assertAlmostEqual(addition(10, 20), 30)
        self.assertAlmostEqual(addition(10, 20), 30.000000000001)
        self.assertNotEqual(addition(10, 20), 31)

    def test04_addition_negative(self):
        if 2 < 3:  # conditional skipping
            self.skipTest("another method for skipping")

        print("In test case - test04_addition_negative")
        assert addition(10, 20) != 31
        self.assertNotEqual(addition(10, 20), 31)


if __name__ == "__main__":
    unittest.main(verbosity=True, failfast=False)
