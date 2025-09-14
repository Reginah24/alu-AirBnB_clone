#!/usr/bin/python3
"""Unittest for FileStorage class."""
import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.storage = FileStorage()
        self.model = BaseModel()
        self.storage.new(self.model)
        self.file_path = "file.json"
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def tearDown(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_all_returns_dict(self):
        self.assertIsInstance(self.storage.all(), dict)

    def test_new_adds_object(self):
        key = f"BaseModel.{self.model.id}"
        self.assertIn(key, self.storage.all())

    def test_save_creates_file(self):
        self.storage.save()
        self.assertTrue(os.path.exists(self.file_path))

    def test_reload_loads_objects(self):
        self.storage.save()
        new_storage = FileStorage()
        new_storage.reload()
        key = f"BaseModel.{self.model.id}"
        self.assertIn(key, new_storage.all())

if __name__ == "__main__":
    unittest.main()
