
import unittest

from rectangle import area, perimeter
class RectangleTestCase(unittest.TestCase):

    def test_area_normal(self):
        self.assertEqual(area(5, 10), 50)
        self.assertEqual(area(0, 10), "erorr")
        self.assertEqual(area(3, "bbc"), "erorr")
        self.assertEqual(area(-90, 10), "erorr")

    def test_perimeter_normal(self):
        self.assertEqual(perimeter(5, 10), 30)
        self.assertEqual(perimeter(0, 10), "erorr")
        self.assertEqual(perimeter(3, "bbc"), "erorr")
        self.assertEqual(perimeter(-8, 10), "erorr")
