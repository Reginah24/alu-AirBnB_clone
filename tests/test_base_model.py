#!/usr/bin/python3
"""Unittests for BaseModel class."""
import unittest
from models.base_model import BaseModel
from datetime import datetime

class TestBaseModel(unittest.TestCase):
    def test_id_type(self):
        obj = BaseModel()
        self.assertIsInstance(obj.id, str)

    def test_created_at_type(self):
        obj = BaseModel()
        self.assertIsInstance(obj.created_at, datetime)

    def test_updated_at_type(self):
        obj = BaseModel()
        self.assertIsInstance(obj.updated_at, datetime)

    def test_str(self):
        obj = BaseModel()
        s = str(obj)
        self.assertIn("BaseModel", s)
        self.assertIn(obj.id, s)

    def test_save(self):
        obj = BaseModel()
        old = obj.updated_at
        obj.save()
        self.assertNotEqual(old, obj.updated_at)

    def test_to_dict(self):
        obj = BaseModel()
        d = obj.to_dict()
        self.assertEqual(d["__class__"], "BaseModel")
        self.assertEqual(d["id"], obj.id)
        self.assertIsInstance(d["created_at"], str)
        self.assertIsInstance(d["updated_at"], str)

    def test_init_from_dict(self):
        obj = BaseModel()
        obj.name = "Test"
        d = obj.to_dict()
        new_obj = BaseModel(**d)
        self.assertEqual(new_obj.id, obj.id)
        self.assertEqual(new_obj.name, "Test")
        self.assertEqual(new_obj.created_at, obj.created_at)
        self.assertEqual(new_obj.updated_at, obj.updated_at)

if __name__ == "__main__":
    unittest.main()
