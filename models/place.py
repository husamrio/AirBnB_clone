#!/usr/bin/python3
"""
 Place Module class
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    Inherits from BaseModel
    Public class attributes:
        amenity_ids:         (list) will be Amenity.id
        number_bathrooms:    (int) 0
        longitude:           (float) 0.0
        user_id:             (str) will be User.id
        city_id:             (str) will be City.id
        description:         (str)
        name:                (str)
        price_by_night:      (int) 0
        number_rooms:        (int) 0
        latitude:            (float) 0.0
        max_guest:           (int) 0
    """
    amenity_ids = []
    number_bathrooms = 0
    longitude = 0.0
    user_id = ""
    city_id = ""
    description = ""
    name = ""
    price_by_night = 0
    number_rooms = 0
    latitude = 0.0
    max_guest = 0
