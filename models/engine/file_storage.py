#!usr/bin/python3
"""Definition of the FileStorage class."""
import json
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    """Serialization to a JSON file and
        deserializing JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return (FileStorage.__objects)

    def new(self, obj):
        obj_n = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(obj_n, obj.id)] = obj

    def save(self):
        dup_obj = FileStorage.__objects
        obj_dict = {obj: dup_obj[obj].to_dict() for obj in dup_obj.keys()}

        with open(FileStorage.__file_path, "w") as f:
            json.dump(obj_dict, f)

    def reload(self):
        try:
            with open(FileStorage.__file_path, "r") as f:
                obj_dict = json.load(f)
                for obj in objects_dict.values():
                    c_name = obj["__class__"]
                    del obj["__class__"]
                    self.new(eval(c_name)(**obj))
        except FileNotFoundError:
            return
