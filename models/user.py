#!/usr/bin/python3
"""Defines the class User"""
from models.base_model import BaseModel


class User(BaseModel):
    """Class that represents a User"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
