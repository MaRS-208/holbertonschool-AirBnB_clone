#!/usr/bin/python3
"""convert the dictionary representation to a JSON string"""


from models.base_model import BaseModel
from models.amenity import Amenity
from models.review import Review
from models.state import State
from models.place import Place
from models.city import City
from models.user import User
import json


class FileStorage:
    """serializes and deserializes an instance to JSON"""
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """returns the dictionary"""
        return self.__objects

    def new(self, obj):
        """sets in dictionary"""
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """serializes the JSON file"""
        new_dict = self.__objects.copy()
        for key, value in new_dict.items():
            new_dict[key] = value.to_dict()
<<<<<<< HEAD
        with open(self.__file_path, "w") as f:
            return f.write(json.dumps(f))
=======
        with open(self.__file.path, w) as f:
            json.dumps(new_dict, f)
>>>>>>> fffd83903a3d0912f950698ec4c519641b0389c4

    def reload(self):
        """Deserialization"""
        with open(self.__file_path, "r") as f:
            tmp = json.load(f)
            for key, value in tmp.items():
                self.all()
                aux = {"Amenity": Amenity,
                       "City": City,
                       "BaseModel": BaseModel,
                       "User": User,
                       "State": State,
                       "Review": Review,
                       "Place": Place}
                self.all()[key] = aux[value["__class__"]](**value)
