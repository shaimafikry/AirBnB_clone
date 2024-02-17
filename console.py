#!/usr/bin/python3
"""my console module"""

import cmd
from models.base_model import BaseModel
import models
from models.user import User
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.state import State

class HBNBCommand(cmd.Cmd):
    """my console class, entry point"""

    classes = {"BaseModel" : BaseModel, "User": User,
                    "City" : City, "State" : State,
                    "Amenity" : Amenity, "Review" : Review,
                    "Place" : Place}

    def do_create(self, line=None):
        """creat an instance from class"""
        if not line:
            print("** class name missing **")
        elif line not in HBNBCommand.classes.keys():
            print("** class doesn't exist **")
        else:
            class_name = HBNBCommand.classes[line]
            ins = class_name()
            class_name.save(ins)
            print (ins.id)


    def do_show(self, line=None):
        """creat an instance from class"""
        words = line.split()
        my_dict = models.storage.all()
        if not line:
            print("** class name missing **")
        elif words[0] not in HBNBCommand.classes.keys():
            print("** class doesn't exist **")
        elif len(words) == 1:
            print("** instance id missing **")
        elif (f"{words[0]}.{words[1]}" not in
           my_dict.keys()):
            print("** no instance found **")
        else: 
            print(my_dict[f"{words[0]}.{words[1]}"])
         
    def do_destroy(self, line=None):
        """destroy an instance from class"""
        words = line.split()
        my_dict = models.storage.all()
        if not line:
            print("** class name missing **")
        elif words[0] not in HBNBCommand.classes.keys():
            print("** class doesn't exist **")
        elif len(words) == 1:
            print("** instance id missing **")
        elif (f"{words[0]}.{words[1]}" not in
           my_dict.keys()):
            print("** no instance found **")
        else: 
            del my_dict[f"{words[0]}.{words[1]}"]
            models.storage.save()

    def do_all(self, line=None):
        """print all instances from class"""
        my_dict = models.storage.all()
        if not line:
            for key in my_dict.keys():
                print(my_dict[key])
        else:
            if line not in HBNBCommand.classes.keys():
                print("** class doesn't exist **")
            else:
                for value in my_dict.values():
                    if value.__class__.__name__ == line:
                        print(value)

    def do_update(self, line=None):
        """creat an instance from class"""
        words = line.split()
        my_dict = models.storage.all()
        if not line:
            print("** class name missing **")
        elif words[0] not in HBNBCommand.classes.keys():
            print("** class doesn't exist **")
        elif len(words) == 1:
            print("** instance id missing **")
        elif (f"{words[0]}.{words[1]}" not in
           my_dict.keys()):
            print("** no instance found **")
        elif len(words) == 2:
            print("** attribute name missing **")
        elif len(words) == 3:
            print("** value missing **")
        else: 
            my_ins = my_dict[f"{words[0]}.{words[1]}"]
            my_ins.__dict__[words[2]] = words[3] 
            models.storage.save()    


    def default(self, line=None):
        """excute dynamic methods"""
        line = line.replace('(', ' ').replace(')', ' ').replace('.', ' ')
        words = line.split()
        print(words)
        my_dict = models.storage.all()

        if len(words) == 2:
            if words[1] == "all":
                print("all")
                self.do_all(words[0])
            elif words[1] == "count":
                counter = 0
                if words[0] not in HBNBCommand.classes.keys():
                    print("** class doesn't exist **")
                else:
                    for value in my_dict.values():
                        if value.__class__.__name__ == words[0]:
                            counter += 1
                    print(counter)
        elif len(words) == 3:
            line = ""
            line = words[0] + " " + words[2]
            print(line)
            if words[1] == "show":
                self.do_show(line)
            elif words[1] == "destroy":
                self.do_destroy(line)
            elif words[1] == "update":
                attributes = words[2].split(', ')
                line = (str(words[0]) + " " +
                        str(attributes[0]) + " " + str(attributes[1])
                        + " " + str(attributes[2]))
                self.do_update(line)
            
        else:
                print("*** Unknown syntax: " + line)
        


    prompt = "(hbnb) "

    def do_help(self, line):
        """help command"""

        print("\nDocumented commands (type help <topic>):\n" +\
        "========================================\n" +\
        "EOF  help  quit\n")

    def do_EOF(self, line):
        """Exit programm"""
        return True

    def emptyline(self):
        """skip, continue"""
        pass

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True
    
if __name__ == '__main__':
    HBNBCommand().cmdloop()
        
