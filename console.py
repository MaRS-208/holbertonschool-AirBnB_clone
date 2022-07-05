#!/usr/bin/python3
"""Write a program called console.py that contains\
the entry point of the command interpreter"""
import cmd
import json


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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
