#!/usr/bin/python3
"""Unittest for Review class."""
import unittest
from models.review import Review

class TestReview(unittest.TestCase):
    def setUp(self):
        self.review = Review()

    def test_place_id_default(self):
        self.assertEqual(self.review.place_id, "")

    def test_user_id_default(self):
        self.assertEqual(self.review.user_id, "")

    def test_text_default(self):
        self.assertEqual(self.review.text, "")

if __name__ == "__main__":
    unittest.main()
