#!/usr/bin/python3
"""Module that contains City class"""

from models.base_model import BaseModel


class City(BaseModel):
    """Class that manages cities instances"""
    state_id = ""
    name = ""
