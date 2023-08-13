#!/usr/bin/python3
"""class user
"""

from models.base_model import BaseModel
import json


class User(BaseModel):
    '''model base class'''

    email = ""
    password = ""
    first_name = ""
    last_name = ""