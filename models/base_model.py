#!/usr/bin/python3
"""Write a class BaseModel that defines all \
common attributes/methods for other classes"""

from datetime import datetime
import uuid
import cmd
import sys


class BaseModel:
    """defines all common attributes/methods for other classes"""
    def __init__(self, *args, **kwargs):
        """initializing"""
        if kwargs is not []:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = key.value
                elif key == "created_at":
                    self.created_at = key.value
                elif key == "updated_at":
                    self.updated_at = key.value
                else:
                    self.id = str(uuid.uuid4())
                    self.created_at = datetime.now()
                    self.updated_at = self.created_at

    def __str__(self):
        """str"""
        return(f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """update the public instance attribute"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dictionary"""
        aux = {}
        for key, item in self.__dict__.items():
            if key == self.updated_at or key == self.created_at:
                aux[key] = item.isoformat()
            else:
                aux[key] = item
        return aux
