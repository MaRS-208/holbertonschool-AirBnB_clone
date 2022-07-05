#!/usr/bin/python3
"""Write a class User that inherits from BaseModel"""


from models.base_model import BaseModel
import json


class User(BaseModel):
    """User"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
