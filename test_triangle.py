import unittest
from triangle import area, perimeter

class TriangleTestCase(unittest.TestCase):

    def test_area_normal(self):
        self.assertEqual(area(5, 10), 25)
        self.assertEqual(area(5, 0), "erorr")
        self.assertEqual(area(3, "bbc"), "erorr")
        self.assertEqual(area(5, -8), "erorr")

    def test_perimeter_normal(self):
        self.assertEqual(perimeter(5, 10, 6), 21)
        self.assertEqual(perimeter(6, 10, 0), "erorr")
        self.assertEqual(perimeter(3, 3, "bbc"), "erorr")
        self.assertEqual(perimeter(6, 10, -8), "erorr")
        self.assertEqual(perimeter(6, 10, 3), "erorr")
