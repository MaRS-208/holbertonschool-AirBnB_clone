#!/usr/bin/python3
"""Write a class BaseModel"""

from datetime import datetime
import models
import uuid


class BaseModel:
    """defines all common attributes/methods for other classes"""

    def __init__(self, *args, **kwargs):
        """initializing"""
        formats = '%Y-%m-%dT%H:%M:%S.%f'
        if kwargs:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "created_at":
                    self.created_at = datetime.strptime(value, formats)
                elif key == "updated_at":
                    self.updated_at = datetime.strptime(value, formats)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """str"""
        return(f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """update the public instance attribute"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary"""
        self.created_at = self.created_at.isoformat()
        self.updated_at = self.updated_at.isoformat()
        self.__dict__["__class__"] = self.__class__.__name__
        return (self.__dict__)
