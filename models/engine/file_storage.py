#!/usr/bin/python3
"""File storage module"""
from json import dumps, loads, dump
from os import path
from models.base_model import BaseModel


class FileStorage:
    """class Filestorage: serialize and deserialize"""
    _file_path = 'file.json'
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        new_dict = {}
        for key, value in FileStorage.__objects.items():
            # """each object has its methods, and to_dict is one of them"""
            # """at most it inherit from basemodel class"""
            new_dict[key] = value.to_dict()

        with open(f'{FileStorage._file_path}', 'w') as file:
            my_string = dumps(new_dict)
            file.write(my_string)

    def reload(self):
        """deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists; otherwise, do nothing."""
        if path.exists(FileStorage._file_path):
            with open(FileStorage._file_path, 'r') as file:
                classes = {
                    "BaseModel": BaseModel
                }

                # """we need to convert dict.values which represent
                #  a dictonary that represent an object"""
                # """we need to restore that object from this dictionary"""
                my_string = file.read()
                if my_string:
                    my_dict = loads(my_string)
                    for cls_id, obj_dict in my_dict.items():
                        class_name = obj_dict.get('__class__')
                        org_class = classes[class_name]
                        my_instance = org_class(**obj_dict)
                        FileStorage.__objects[cls_id] = my_instance
