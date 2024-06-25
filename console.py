#!/usr/bin/python3
"""my console module, the entry point of the command interpreter:"""

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
    """the entry point of the command interpreter:"""
    prompt  = "(hbnb)"

    def do_EOF(self, line):
        """ctrl + d > to exit the programm"""
        print()
        return True
    
    def do_quit(self, line):
        """Quit command to exit the program"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
