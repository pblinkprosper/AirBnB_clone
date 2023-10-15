#!usr/bin/python3
"""Definition of the BaseModel class."""
import uuid
from datetime import datetime
import models


class BaseModel:
    """Defines all common attributes/methods for other classes."""

    def __init__(self, *args, **kwargs):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs):
            iso_format = "%Y-%m-%dT%H:%M:%S.%f"
            for key, value in kwargs.items():
                if key in ["created_at", "updated_at"]:
                    self.__dict__[key] = datetime.strptime(value, iso_format)
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

    # public instance methods
    def save(self):
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        dup_dict = self.__dict__.copy()
        dup_dict["created_at"] = self.created_at.isoformat()
        dup_dict["updated_at"] = self.updated_at.isoformat()
        dup_dict["__class__"] = self.__class__.__name__

        return (dup_dict)

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
