#!/usr/bin/python3

"""Place module inherit from Basemodel module"""

from models.base_model import BaseModel
import models

class Place(BaseModel):
    """my Place class"""

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = 0.0
