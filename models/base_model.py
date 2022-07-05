#!/usr/bin/python3
"""Import"""

import uuid
from datetime import datetime
import cmd
import sys

"""Import"""


class BaseModel:
    """Create"""
    def __init__(self, id):
        """self"""
        self.id = str(uuid.uuid4())
        created_at = datetime.now()
        updated_at = self.created_at.datetime.now()

    def __str__(self):
        """str"""
        return(f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """update the public instance attribute"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dictionary"""
        self.created_at = created_at.isoformat()
        self.updated_at = updated_at.isoformat()
