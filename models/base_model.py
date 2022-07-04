#!/usr/bin/python3
"""Write a class BaseModel that defines all common attributes/methods for other classes"""

from datetime import datetime
import uuid
import cmd
import sys


class BaseModel:
    """defines all common attributes/methods for other classes"""
    def __init__(self):
        """initializing"""
        self.id = str(uuid.uuid4())
        created_at = datetime.now()
        updated_at = created_at

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
            if key == self.created_at or key == self.updated_at:
                self.created_at = self.created_at.isoformat()
                self.updated_at = self.updated_at.isoformat()
            aux[key] = item


