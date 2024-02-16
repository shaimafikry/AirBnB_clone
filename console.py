#!/usr/bin/python3
"""my console module"""

import cmd

class HBNBCommand(cmd.Cmd):
    """my console class, entry point"""

    intro = "welcome to my console interrpreter"
    prompt = "(hbnb)"

    def do_help(self, line):
        """help command"""
        if line == "quit":
            print("Quit command to exit the program")
        else:
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
        
