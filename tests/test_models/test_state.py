#!/usr/bin/python3
"""Unittest for State class."""
import unittest
from models.state import State

class TestState(unittest.TestCase):
    def setUp(self):
        self.state = State()

    def test_name_default(self):
        self.assertEqual(self.state.name, "")

if __name__ == "__main__":
    unittest.main()
