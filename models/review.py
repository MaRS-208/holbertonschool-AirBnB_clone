#!/usr/bin/python3
"""Write a class Review that inherits from BaseModel"""


from models.base_model import BaseModel


class Review(BaseModel):
    """Review"""
    place_id: ""
    user_id: ""
    text: ""
