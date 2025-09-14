#!/usr/bin/python3
"""
BaseModel module for AirBnB clone project.

This module contains the BaseModel class which defines all common
attributes/methods for other classes.
"""

import uuid
from datetime import datetime


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
            # Import here to avoid circular import
            from models import storage
            storage.new(self)

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
        # Import here to avoid circular import
        from models import storage
        storage.save()

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