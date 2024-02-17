#!/usr/bin/python3

"""user module inherit from Basemodel module"""

from models.base_model import BaseModel
import models

class User(BaseModel):
    """my user class"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
