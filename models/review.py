#!/usr/bin/python3
"""
Review Module class
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    BaseModel Inherits from
    Class Public attributes:
        text:                (str)
        user_id:             (str) will be User.id
        place_id:            (str) will be Place.id
    """
    place_id = ""
    user_id = ""
    text = ""