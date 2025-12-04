import unittest
from square import area, perimeter
class SquareTestCase(unittest.TestCase):

    def test_area_normal(self):
        self.assertEqual(area(5), 25)
        self.assertEqual(area(0), "erorr")
        self.assertEqual(area("bbc"), "erorr")
        self.assertEqual(area(-9), "erorr")

    def test_perimeter_normal(self):
        self.assertEqual(perimeter(5), 20)
        self.assertEqual(perimeter(0), "erorr")
        self.assertEqual(perimeter("bbc"), "erorr")
        self.assertEqual(perimeter(-8), "erorr")
