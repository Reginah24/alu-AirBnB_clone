
#!/usr/bin/python3
"""Defines the FileStorage class."""

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import os


class FileStorage:
    """Serializes instances to a JSON file and deserializes back to instances."""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        obj_dict = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(obj_dict, f)

    def reload(self):
        if not os.path.exists(FileStorage.__file_path):
            return
        try:
            with open(FileStorage.__file_path, "r") as f:
                obj_dict = json.load(f)
                for key, value in obj_dict.items():
                    cls_name = value.get("__class__")
                    if cls_name == "BaseModel":
                        FileStorage.__objects[key] = BaseModel(**value)
                    elif cls_name == "User":
                        FileStorage.__objects[key] = User(**value)
                    elif cls_name == "State":
                        FileStorage.__objects[key] = State(**value)
                    elif cls_name == "City":
                        FileStorage.__objects[key] = City(**value)
                    elif cls_name == "Amenity":
                        FileStorage.__objects[key] = Amenity(**value)
                    elif cls_name == "Place":
                        FileStorage.__objects[key] = Place(**value)
                    elif cls_name == "Review":
                        FileStorage.__objects[key] = Review(**value)
        except Exception:
            pass
