#!/usr/bin/python3

"""Review module inherit from Basemodel module"""

from models.base_model import BaseModel
import models


class Review(BaseModel):
    """my Review class"""

    place_id = ""
    user_id = ""
    text = ""
