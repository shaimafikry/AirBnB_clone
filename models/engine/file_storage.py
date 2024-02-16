#!/usr/bin/python3
"""File storage module"""

from models.base_model import BaseModel
import json
import os
from datetime import datetime
class FileStorage:
    """class Filestorage: serialize and deserialize"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """doc"""
        return FileStorage.__objects

    def new(self, obj):
        """doc"""
        x = obj.__class__.__name__
        id = obj.__dict__.get("id")
        FileStorage.__objects[f"{x}.{id}"] = obj

    def save(self):
        """doc"""
        dict = {}
        for key, obj in FileStorage.__objects.items():
            dict[key] = obj.to_dict()

        with open(FileStorage.__file_path, "w") as file:
            my_string = json.dumps(dict)
            file.write(my_string)
    
    def reload(self):
        """doc"""
        file_path = FileStorage.__file_path
        if os.path.exists(file_path):
            with open(file_path, "r") as file:
                my_string = file.read()
                if my_string:
                    my_classes = {"BaseModel" : BaseModel}
                    FileStorage.__objects = json.loads(my_string)
                    for key, dict in FileStorage.__objects.items():
                        #class_name returned as string
                        class_name = dict.pop("__class__")
                        #update class_name to point to class_name exactly
                        class_name = my_classes[class_name]
                        ins_from_dict = class_name(**dict)
                        FileStorage.__objects[key] = ins_from_dict
