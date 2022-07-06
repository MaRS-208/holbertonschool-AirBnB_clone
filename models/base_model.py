#!/usr/bin/python3
"""Write a class BaseModel that defines all \
common attributes/methods for other classes"""

from datetime import datetime
from models import storage
import json
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

    def __str__(self):
        """str"""
        return(f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """update the public instance attribute"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """returns a dictionary"""
        aux = self.__dict__.copy()
        aux["created_at"] = self.created_at.isoformat()
        aux["updated_at"] = self.updated_at.isoformat()
        aux['__class__'] = self.__class__.__name__
        return aux
