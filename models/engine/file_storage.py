#!/usr/bin/python3
"""convert the dictionary representation to a JSON string"""

import json


class FileStorage:
    """Create"""
    def __init__(self):
        self.__file_path = file.json
        self.__objetcs = {}

    def all(self):
        """returns the dictionary"""
        return (self.__objects)

    def new(self, obj):
        """sets in dictionary"""
        self.__objects[f"{obj.__class__.name}.{obj.id}"] = obj

    def save(self):
        """serializes the JSON file"""
        new_dict = self.__objects.copy()
        for key, value in new_dict.items():
            new_dict[key] = value.to_dict()
        with open(self.__file.path, w) as f:
            json.dumps(__objects)
