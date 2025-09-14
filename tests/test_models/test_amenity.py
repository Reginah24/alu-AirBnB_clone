#!/usr/bin/python3
"""Unittest for Amenity class."""
import unittest
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):
    def setUp(self):
        self.amenity = Amenity()

    def test_name_default(self):
        self.assertEqual(self.amenity.name, "")

if __name__ == "__main__":
    unittest.main()
