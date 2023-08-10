#!/usr/bin/python3
"""File storage module"""

import json

class FileStorage():
	__file_path = "file.json"
	__objects = {}

	def all(self):
		return FileStorage.__objects

	def new(self, obj):
		new_key = obj.__class__.__name__ + "." + obj.id
		FileStorage.__objects[new_key] = obj

	def save(self):
		d = {}
		for key, value in self.__objects.item():
			d[key] = value.to_dict()
		with open(FileStorage.__file_path, 'w', encoding="utf-8") as my_file:
			json.dump(d, my_file)

	def reload(self):
		try:
			with open(self.__file_path, encoding="utf-8") as my_file:
				d = json.load(my_file)
				for key, value in d.items():
					cls = value["__class__"]
					FileStorage.__objects[key] = eval(cls)(**value)
		except FileNotFoundError:
			pass
