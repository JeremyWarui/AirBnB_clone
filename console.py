#!/usr/bin/python3
import cmd
"""
class for the console and its commands
"""


class HBNBCommand(cmd.Cmd):
    """
    command interpreter
    """
    prompt = "(hbnb) "

    def do_quit(self, line):
        """ Quit command to exit the program """
        return True

    def do_EOF(self, line):
        """ EOF command to exit the cmd """
        return True

    def emptyline(self):
        """ Overwrite default behavior to repeat last command"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
