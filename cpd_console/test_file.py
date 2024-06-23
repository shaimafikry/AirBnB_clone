#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel
from models.city import City

all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Create a new object --")
my_model = BaseModel()
my_model.name = "My_First_Model"
my_model.my_number = 89
my_model.save()
print(my_model)

print("-----")
my_model = City()
my_model.name = "My_First_CITY"
my_model.my_number = 89
my_model.save()
print(my_model)
