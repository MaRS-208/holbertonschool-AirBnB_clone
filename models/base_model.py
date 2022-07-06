#!/usr/bin/python3
"""Write a class BaseModel"""

from datetime import datetime
from models import storage
import uuid


class BaseModel:
    """defines all common attributes/methods for other classes"""

    def __init__(self, *args, **kwargs):
        """initializing"""
        is_format = '%Y-%m-%dT%H:%M:%S.%f'
        if kwargs:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "created_at":
                    self.created_at = datetime.strptime(value, is_format)
                elif key == "updated_at":
                    self.updated_at = datetime.strptime(value, is_format)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)

    def __str__(self):
        """str"""
        return(f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """update the public instance attribute"""
        self.updated_at = datetime.now()
        updated_at = datetime.strptime('%Y-%m-%dT%H:%M:%S.%f')
        storage.save()

    def to_dict(self):
        """returns a dictionary"""
        aux = {"__class__": type(self).__name__}
        for key in self.__dict__:
            if key == "created_at" or key == "updated_at":
                aux[key] == self.__dict__[key].isoformat()
            else:
                aux[key] = self.__dict__[key]
        return aux
