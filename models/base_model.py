#!/usr/bin/python3
"""Module for Base class
Contains the Base class for the AirBnB clone console.
"""

import uuid
from datetime import datetime

class BaseModel:
    """A base class for all other classes"""

    def __str__(self):
        """Return a string representation of the instance"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Update the updated_at attribute with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Return a dictionary representation of the instance"""
        dictionary = self.__dict__.copy()
        dictionary["__class__"] = self.__class__.__name__ 
        dictionary["created_at"] = self.created_at.isoformat() 
        dictionary["updated_at"] = self.updated_at.isoformat() 
        return dictionary
