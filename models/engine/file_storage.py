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
        new_item = {obj.__class__.__name__.id: obj}
        FileStorage.__objects.update(new_item)

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)
        to hold objects after turn them too dictionary"""
        j_dict ={}
        for k, v in self.__objects.items():
            j_dict[k] = v.to_dict()
        with open (FileStorage.__file_path, "w", encoding="utf-8") as f:
            json.dump(j_dict, f)

    def reload(self):
        """ deserializes the JSON file to _objects (only if the JSON file (_file_path) exists otherwise, do nothing. If the file doesn’t exist, no exception should be raised"""
        try:
            with open (FileStorage.__file_path, "r", encoding="utf-8") as f:
               objects = json.load(f)
               for k, v in objects.items():
                   FileStorage.__objects[k] = self(**v)
        except FileNotFoundError:
            pass
