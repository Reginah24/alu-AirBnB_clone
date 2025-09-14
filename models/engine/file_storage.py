#!/usr/bin/python3
"""FileStorage module for AirBnB clone project."""
import json
from models.base_model import BaseModel
import os

class FileStorage:
    """Serializes instances to a JSON file and deserializes back to instances."""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file."""
        obj_dict = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(obj_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects, if it exists."""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review
        classes = {
            'BaseModel': BaseModel,
            'User': User,
            'State': State,
            'City': City,
            'Amenity': Amenity,
            'Place': Place,
            'Review': Review
        }
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as f:
                obj_dict = json.load(f)
                for key, value in obj_dict.items():
                    cls_name = value.get('__class__')
                    cls = classes.get(cls_name)
                    if cls:
                        FileStorage.__objects[key] = cls(**value)
