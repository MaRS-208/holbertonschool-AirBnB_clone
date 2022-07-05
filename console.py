#!/usr/bin/python3
"""Write a program called console.py that contains\
the entry point of the command interpreter"""
import cmd
import json
from models.amenity import Amenity
from models.city import City
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.review import Review
from models.place import Place


class HBNBCommand(cmd.Cmd):
    """entry point of the command interpreter"""
    prompt = "(hbnb) "

    def emptyline(self):
        """an empty line + ENTER shouldn’t execute anything"""
        pass

    def do_quit(self, arg):
        """quit to exit"""
        return True

    def do_EOF(self, arg):
        """EOF error"""
        return True

    def do_create(self, arg):
        """create"""
        aux = {"Amenity": Amenity,
               "City": City,
               "BaseModel": BaseModel,
               "User": User,
               "State": State,
               "Review": Review,
               "Place": Place}
        obj = aux[arg]()
        obj.save()
        print(obj)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
