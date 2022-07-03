#!/usr/bin/python3
"""Import"""

import uuid
from datetime import datetime
import cmd
import sys

class BaseModel:
    """Create"""

    def __init__(self, id):
        """self"""
        self.id = id

        id = uuid.uuid4()
        created_at = datetime.now()
        updated_at = datetime.now()
       
    @classmethod
    def __str__(self):
        """str"""
        return(f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """update the public instance attribute"""
    self.save = self
    self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dictionary"""
        created_at = datetime.now().isoformat()
        updated_at = datetime.now().isoformat()
        datetime.datetime.strptime('2017-06-14T22:31:03.285259', '%Y-%m-%dT%H:%M:%S.%f')


