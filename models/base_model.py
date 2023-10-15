#!/usr/bin/python3
"""
This class defines all common methods and attributes of other classes
"""
import uuid
import models
from datetime import datetime


class BaseModel:
    """BaseModel Class"""

    def __init__(self, *args, **kwargs):
        """Initialize the BaseModel class"""

        self.id = str(uuid.uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

        if len(kwargs):
            d_format = "%Y-%m-%dT%H:%M:%S.%f"
            for key, value in kwargs.items():
                if key in ["created_at", "updated_at"]:
                    self.__dict__[key] = datetime.strptime(value, d_format)
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

        def save(self):
            """
            Update values updated_at with current datetime
            """
            self.updated_at = datetime.today()
            models.storage.save()

        def to_dict(self):
            """
            Returns dictionary containing all keys and
            values of __dict__ for the instance
            """
            dup_dict = self.__dict__.copy()
            dup_dict["created_at"] = self.created_at.isoformat()
            dup_dict["updated_at"] = self.updated_at.isoformat()
            dup_dict["__class__"] = self.__class__.__name__
            return dup_dict

        def __str__(self):
            """
            Return the str representation of a BaseModel instance
            """

            return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
