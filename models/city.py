#!/usr/bin/python3
"""
City Module class
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    BaseModel Inherits from
     class Public attributes:
        name:     (str)
        state_id: (str) will be State.id
    """
    state_id = ""
    name = ""
