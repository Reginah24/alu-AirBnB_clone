#!/usr/bin/python3
"""
FileStorage module for AirBnB clone project.

This module contains the FileStorage class that handles
serialization and deserialization of objects to/from JSON files.
"""

import json
import os


class FileStorage:
    """
    Serializes instances to a JSON file and deserializes JSON file to instances.
    
    Attributes:
        __file_path (str): Path to the JSON file
        __objects (dict): Dictionary storing all objects by <class name>.id
    """
    
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Return the dictionary __objects.
        
        Returns:
            dict: Dictionary containing all stored objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Set in __objects the obj with key <obj class name>.id.
        
        Args:
            obj: Object instance to store
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serialize __objects to the JSON file (path: __file_path)."""
        json_objects = {}
        for key, obj in FileStorage.__objects.items():
            json_objects[key] = obj.to_dict()
        
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            json.dump(json_objects, f)

    def reload(self):
        """
        Deserialize the JSON file to __objects.
        
        Only if the JSON file (__file_path) exists; otherwise, do nothing.
        If the file doesn't exist, no exception should be raised.
        """
        try:
            if os.path.exists(FileStorage.__file_path):
                with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                    obj_dict = json.load(f)
                    
                for key, value in obj_dict.items():
                    class_name = value["__class__"]
                    # Import classes dynamically to avoid circular imports
                    if class_name == "BaseModel":
                        from models.base_model import BaseModel
                        obj = BaseModel(**value)
                    elif class_name == "User":
                        from models.user import User
                        obj = User(**value)
                    elif class_name == "State":
                        from models.state import State
                        obj = State(**value)
                    elif class_name == "City":
                        from models.city import City
                        obj = City(**value)
                    elif class_name == "Amenity":
                        from models.amenity import Amenity
                        obj = Amenity(**value)
                    elif class_name == "Place":
                        from models.place import Place
                        obj = Place(**value)
                    elif class_name == "Review":
                        from models.review import Review
                        obj = Review(**value)
                    else:
                        continue
                    
                    FileStorage.__objects[key] = obj
        except (FileNotFoundError, json.JSONDecodeError):
            pass


# ============ models/__init__.py ============
#!/usr/bin/python3
"""
Init file for models package.

This module creates a unique FileStorage instance for the application.
"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()


# ============ models/engine/__init__.py ============
#!/usr/bin/python3
"""Init file for engine package."""


# ============ models/base_model.py ============
#!/usr/bin/python3
"""
BaseModel module for AirBnB clone project.

This module contains the BaseModel class which defines all common
attributes/methods for other classes.
"""

import uuid
from datetime import datetime
import models


class BaseModel:
    """
    Base class that defines all common attributes/methods for other classes.
    
    Attributes:
        id (str): Unique identifier for each instance
        created_at (datetime): Time when instance was created
        updated_at (datetime): Time when instance was last updated
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize a new BaseModel instance.
        
        Args:
            *args: Variable length argument list (unused)
            **kwargs: Arbitrary keyword arguments for instance recreation
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                elif key in ['created_at', 'updated_at']:
                    setattr(self, key, datetime.strptime(
                        value, '%Y-%m-%dT%H:%M:%S.%f'))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        Return string representation of BaseModel instance.
        
        Returns:
            str: String representation in format [<class>] (<id>) <dict>
        """
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Update updated_at with current datetime and save to storage.
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Return dictionary representation of BaseModel instance.
        
        Returns:
            dict: Dictionary containing all keys/values of instance __dict__
                  plus class name and ISO formatted datetime strings
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict


# ============ Additional Model Classes ============
#!/usr/bin/python3
"""User module."""
from models.base_model import BaseModel


class User(BaseModel):
    """User class that inherits from BaseModel."""
    
    email = ""
    password = ""
    first_name = ""
    last_name = ""


#!/usr/bin/python3
"""State module."""
from models.base_model import BaseModel


class State(BaseModel):
    """State class that inherits from BaseModel."""
    
    name = ""


#!/usr/bin/python3
"""City module."""
from models.base_model import BaseModel


class City(BaseModel):
    """City class that inherits from BaseModel."""
    
    state_id = ""
    name = ""


#!/usr/bin/python3
"""Amenity module."""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity class that inherits from BaseModel."""
    
    name = ""


#!/usr/bin/python3
"""Place module."""
from models.base_model import BaseModel


class Place(BaseModel):
    """Place class that inherits from BaseModel."""
    
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []


#!/usr/bin/python3
"""Review module."""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review class that inherits from BaseModel."""
    
    place_id = ""
    user_id = ""
    text = ""