#!/usr/bin/python3
"""File storage module"""

import json


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
        for key, value in self.__objects.item():
            d[key] = value.to_dict()
        with open(FileStorage.__file_path, 'w', encoding="utf-8") as my_file:
            json.dump(d, my_file)

    def reload(self):
        """Reloads objects from a file"""
        try:
            with open(self.__file_path, encoding="utf-8") as my_file:
                d = json.load(my_file)
                for key, value in d.items():
                    cls = value["__class__"]
                    FileStorage.__objects[key] = eval(cls)(**value)
        except FileNotFoundError:
            pass
