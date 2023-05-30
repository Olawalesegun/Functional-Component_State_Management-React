import unittest
from oop.area_ import area_of_c
from math import pi


class MyTestCase(unittest.TestCase):
    def test_area_of_circle_works(self):
        self.assertAlmostEqual(area_of_c(1), pi)
        self.assertAlmostEqual(area_of_c(0), 0)

    def test_area_function_reject_negative_value(self):
        self.assertRaises(ValueError, area_of_c, -2)

    def test_area_function_reject_string_value(self):
        self.assertRaises(TypeError, area_of_c, "ASA")

    # def test_something(self):
    #     self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
