import unittest
from circle import area, perimeter
class CircleTestCase(unittest.TestCase):

    def test_area_normal(self):
        self.assertEqual(area(5), 78.53981633974483)
        self.assertEqual(area(0), "erorr")
        self.assertEqual(area("bbc"), "erorr")
        self.assertEqual(area(-8), "erorr")

    def test_perimeter_normal(self):
        self.assertEqual(perimeter(5), 31.41592653589793)
        self.assertEqual(perimeter(0), "erorr")
        self.assertEqual(perimeter("bbc"),"erorr")
        self.assertEqual(perimeter(-9), "erorr")
        
