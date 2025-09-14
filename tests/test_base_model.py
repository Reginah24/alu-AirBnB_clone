#!/usr/bin/python3
"""Unittest for BaseModel class."""
import unittest
from models.base_model import BaseModel
from datetime import datetime

class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.model = BaseModel()

    def test_id_is_str(self):
        self.assertIsInstance(self.model.id, str)

    def test_created_at_is_datetime(self):
        self.assertIsInstance(self.model.created_at, datetime)

    def test_updated_at_is_datetime(self):
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_to_dict_contains_class(self):
        d = self.model.to_dict()
        self.assertIn("__class__", d)
        self.assertEqual(d["__class__"], "BaseModel")

    def test_save_updates_updated_at(self):
        old_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(old_updated_at, self.model.updated_at)

    def test_str(self):
        s = str(self.model)
        self.assertIn("BaseModel", s)
        self.assertIn(self.model.id, s)

    def test_init_from_dict(self):
        d = self.model.to_dict()
        new_model = BaseModel(**d)
        self.assertEqual(new_model.id, self.model.id)
        self.assertEqual(new_model.created_at, self.model.created_at)
        self.assertEqual(new_model.updated_at, self.model.updated_at)

if __name__ == "__main__":
    unittest.main()
