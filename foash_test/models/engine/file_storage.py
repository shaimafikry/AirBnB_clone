#!/usr/bin/python3
"""File storage module"""


from models.base_model import BaseModel
import json


class FileStorage:
    """class Filestorage: serialize and deserialize"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        try:
            with open(self.__file_path, "r") as file:
                self.__objects = json.load(file)
        except FileNotFoundError:
            pass
        return self.__objects
    
    def new(self, obj):
        self.__objects[f"{BaseModel.id}"] = obj

    def save(self):
        json.dump(self.__objects, self.__file_path)

    def reload(self):
        try:
            with open(self.__file_path, "r") as file:
                self.__objects = json.load(file)
        except FileNotFoundError:
            pass
