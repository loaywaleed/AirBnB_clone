#!/usr/bin/python3
"""File storage module"""

import datetime
import json
import os


class FileStorage():
    """Class that adds storage functionality"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Function that shows all created objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Creates new object"""
        new_key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[new_key] = obj

    def save(self):
        """Saves objects to file"""
        d = {}
        for key, value in self.__objects.items():
            d[key] = value.to_dict()
        with open(FileStorage.__file_path, 'w', encoding="utf-8") as my_file:
            json.dump(d, my_file)

    def reload(self):
        """Reloads objects from a file"""
        try:
            if not os.path.isfile(FileStorage.__file_path):
                return
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                obj_dict = json.load(f)
                obj_dict = {k: self.classes()[v["__class__"]]
                            (**v) for k, v in obj_dict.items()}
                FileStorage.__objects = obj_dict
        except FileNotFoundError:
            pass

    def classes(self):
        from models.base_model import BaseModel
        classes = {"BaseModel": BaseModel}
        return classes

    def attributes(self):
        """Returns the valid attributes and their types for classname"""
        attributes = {
            "BaseModel":
                     {"id": str,
                      "created_at": datetime.datetime,
                      "updated_at": datetime.datetime},
            "User":
                     {"email": str,
                      "password": str,
                      "first_name": str,
                      "last_name": str},
            "State":
                     {"name": str},
            "City":
                     {"state_id": str,
                      "name": str},
            "Amenity":
                     {"name": str},
            "Place":
                     {"city_id": str,
                      "user_id": str,
                      "name": str,
                      "description": str,
                      "number_rooms": int,
                      "number_bathrooms": int,
                      "max_guest": int,
                      "price_by_night": int,
                      "latitude": float,
                      "longitude": float,
                      "amenity_ids": list},
            "Review":
            {"place_id": str,
                         "user_id": str,
                         "text": str}
        }
        return attributes
