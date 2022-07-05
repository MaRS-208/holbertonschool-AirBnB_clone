#!/usr/bin/python3
"""convert the dictionary representation to a JSON string"""

import json
from models.amenity import Amenity
from models.city import City
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.review import Review
from models.place import Place


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
            json.dump(self._objects, f)

    def reload(self):
        """Deserialization"""
        with open(self.__file_path, r) as f:
            tmp = json.load(f)
            for key, value in tmp:
                self.all()
            aux = {"Amenity": Amenity,
                    "City": City,
                    "BaseModel": BaseModel,
                    "User": User,
                    "State": State,
                    "Review": Review,
                    "Place": Place}
            self.all()[key] = aux[value.__class__](**value)
