#!/usr/bin/python3
"""Unittest for User class."""
import unittest
from models.user import User

class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User()

    def test_email_default(self):
        self.assertEqual(self.user.email, "")

    def test_password_default(self):
        self.assertEqual(self.user.password, "")

    def test_first_name_default(self):
        self.assertEqual(self.user.first_name, "")

    def test_last_name_default(self):
        self.assertEqual(self.user.last_name, "")

if __name__ == "__main__":
    unittest.main()
