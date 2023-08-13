#!/usr/bin/python3
"""Module that contains Review class"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Class that manages reviews"""
    place_id = ""
    user_id = ""
    text = ""
