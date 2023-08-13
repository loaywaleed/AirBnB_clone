#!/usr/bin/python3
"""Module that contains a user class"""

from models.base_model import BaseModel


class User(BaseModel):
    "Class for managing user instances"
    email = ""
    password = ""
    first_name = ""
    last_name = ""
