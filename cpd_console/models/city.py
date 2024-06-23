#!/usr/bin/python3

"""city module inherit from Basemodel module"""

from models.base_model import BaseModel
import models


class City(BaseModel):
    """my City class"""

    name = ""
    state_id = ""
