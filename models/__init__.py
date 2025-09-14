# models/__init__.py
"""Initializes the models package and creates storage instance."""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
