#!/usr/bin/python3
"""Import"""

import uuid
from datetime import datetime
import cmd
import sys
from models import storage

"""Import"""


class BaseModel:
    """Create"""
    def __init__(self, id):
        """self"""
        self.id = str(uid.uuid4())
        created_at = datetime.now()
        updated_at = datetime.now()
        datetime.strptime('2017-06-14T22:31:03.285259', '%Y-%m-%dT%H:%M:%S.%f')

    @classmethod
    def __str__(self):
        """str"""
        return(f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """update the public instance attribute"""
        self.save = save
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary"""
        self.created_at = created_at.isoformat()
        self.updated_at = updated_at.isoformat()
