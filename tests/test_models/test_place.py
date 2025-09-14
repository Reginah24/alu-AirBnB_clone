#!/usr/bin/python3
"""Unittest for Place class."""
import unittest
from models.place import Place

class TestPlace(unittest.TestCase):
    def setUp(self):
        self.place = Place()

    def test_city_id_default(self):
        self.assertEqual(self.place.city_id, "")

    def test_user_id_default(self):
        self.assertEqual(self.place.user_id, "")

    def test_name_default(self):
        self.assertEqual(self.place.name, "")

    def test_description_default(self):
        self.assertEqual(self.place.description, "")

    def test_number_rooms_default(self):
        self.assertEqual(self.place.number_rooms, 0)

    def test_number_bathrooms_default(self):
        self.assertEqual(self.place.number_bathrooms, 0)

    def test_max_guest_default(self):
        self.assertEqual(self.place.max_guest, 0)

    def test_price_by_night_default(self):
        self.assertEqual(self.place.price_by_night, 0)

    def test_latitude_default(self):
        self.assertEqual(self.place.latitude, 0.0)

    def test_longitude_default(self):
        self.assertEqual(self.place.longitude, 0.0)

    def test_amenity_ids_default(self):
        self.assertEqual(self.place.amenity_ids, [])

if __name__ == "__main__":
    unittest.main()
