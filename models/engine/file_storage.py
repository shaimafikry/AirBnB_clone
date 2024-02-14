#!/usr/bin/python3
""" file storage to store all the date"""
import json


class FileStorage():
    """class stotage to represent data to json file
objects: to store class name.id 
file_path: to hold the name of json file
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        self.__objects[obj.id] = obj.__dict__

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        with open (self.__file_path, "w", encoding="utf-8") as f:
            json.dump(self.__objects, f)

    def reload(self):
        """ deserializes the JSON file to _objects (only if the JSON file (_file_path) exists otherwise, do nothing. If the file doesn’t exist, no exception should be raised"""
        try:
            with open (self.__file_path, "r", encoding="utf-8") as f:
                self.__objects = json.load(f)
        except FileNotFoundError:
            pass
