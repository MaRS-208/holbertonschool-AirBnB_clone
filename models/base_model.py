#!/usr/bin/python3
"""Write a class BaseModel that defines all \
common attributes/methods for other classes"""

from datetime import datetime
import uuid
from models import storage


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
        self.created_at = self.created_at.isoformat()
        self.updated_at = self.updated_at.isoformat()
        self.__dict__["__class__"] = self.__class__.__name__
        return(self.__dict__)
