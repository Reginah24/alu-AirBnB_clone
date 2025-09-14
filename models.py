#!/usr/bin/python3
"""
Base model module for AirBnB clone project.

This module contains the BaseModel class which defines all common
attributes/methods for other classes in the AirBnB clone project.
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
        Update the updated_at attribute with current datetime and save to storage.
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


class User(BaseModel):
    """
    User class that inherits from BaseModel.
    
    Attributes:
        email (str): User's email address
        password (str): User's password
        first_name (str): User's first name
        last_name (str): User's last name
    """

    def __init__(self, *args, **kwargs):
        """Initialize User instance."""
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
        super().__init__(*args, **kwargs)


class State(BaseModel):
    """
    State class that inherits from BaseModel.
    
    Attributes:
        name (str): Name of the state
    """

    def __init__(self, *args, **kwargs):
        """Initialize State instance."""
        self.name = ""
        super().__init__(*args, **kwargs)


class City(BaseModel):
    """
    City class that inherits from BaseModel.
    
    Attributes:
        state_id (str): State ID that the city belongs to
        name (str): Name of the city
    """

    def __init__(self, *args, **kwargs):
        """Initialize City instance."""
        self.state_id = ""
        self.name = ""
        super().__init__(*args, **kwargs)


class Amenity(BaseModel):
    """
    Amenity class that inherits from BaseModel.
    
    Attributes:
        name (str): Name of the amenity
    """

    def __init__(self, *args, **kwargs):
        """Initialize Amenity instance."""
        self.name = ""
        super().__init__(*args, **kwargs)


class Place(BaseModel):
    """
    Place class that inherits from BaseModel.
    
    Attributes:
        city_id (str): City ID where the place is located
        user_id (str): User ID of the place owner
        name (str): Name of the place
        description (str): Description of the place
        number_rooms (int): Number of rooms
        number_bathrooms (int): Number of bathrooms
        max_guest (int): Maximum number of guests
        price_by_night (int): Price per night
        latitude (float): Latitude coordinate
        longitude (float): Longitude coordinate
        amenity_ids (list): List of Amenity IDs
    """

    def __init__(self, *args, **kwargs):
        """Initialize Place instance."""
        self.city_id = ""
        self.user_id = ""
        self.name = ""
        self.description = ""
        self.number_rooms = 0
        self.number_bathrooms = 0
        self.max_guest = 0
        self.price_by_night = 0
        self.latitude = 0.0
        self.longitude = 0.0
        self.amenity_ids = []
        super().__init__(*args, **kwargs)


class Review(BaseModel):
    """
    Review class that inherits from BaseModel.
    
    Attributes:
        place_id (str): Place ID being reviewed
        user_id (str): User ID of the reviewer
        text (str): Review text content
    """

    def __init__(self, *args, **kwargs):
        """Initialize Review instance."""
        self.place_id = ""
        self.user_id = ""
        self.text = ""
        super().__init__(*args, **kwargs)


def validate_email(email):
    """
    Validate email format.
    
    Args:
        email (str): Email address to validate
        
    Returns:
        bool: True if email format is valid, False otherwise
    """
    import re
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))


def format_datetime(dt):
    """
    Format datetime object to ISO string.
    
    Args:
        dt (datetime): Datetime object to format
        
    Returns:
        str: ISO formatted datetime string
    """
    return dt.isoformat() if isinstance(dt, datetime) else str(dt)


def parse_datetime(dt_string):
    """
    Parse ISO datetime string to datetime object.
    
    Args:
        dt_string (str): ISO formatted datetime string
        
    Returns:
        datetime: Parsed datetime object
        
    Raises:
        ValueError: If string format is invalid
    """
    try:
        return datetime.strptime(dt_string, '%Y-%m-%dT%H:%M:%S.%f')
    except ValueError as e:
        raise ValueError(f"Invalid datetime format: {dt_string}") from e


# Module-level constants
MAX_STRING_LENGTH = 128
DEFAULT_AMENITIES = [
    'WiFi', 'Kitchen', 'Parking', 'Air conditioning',
    'Heating', 'TV', 'Washer', 'Dryer'
]

# Version information
__version__ = "1.0.0"
__author__ = "AirBnB Clone Team"
__email__ = "team@airbnbclone.com"