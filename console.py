#!/usr/bin/python3
"""
Command line interpreter for AirBnB clone project.

This module contains the HBNBCommand class which implements
a command line interface for managing AirBnB clone objects.
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """
    Command line interpreter class for AirBnB clone.
    
    This class inherits from cmd.Cmd and implements various
    commands for managing objects in the AirBnB clone application.
    """
    
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program."""
        return True

    def emptyline(self):
        """Override emptyline method to do nothing on empty line."""
        pass

    def help_quit(self):
        """Help documentation for quit command."""
        print("Quit command to exit the program")

    def help_EOF(self):
        """Help documentation for EOF command."""
        print("EOF command to exit the program")


if __name__ == '__main__':
    HBNBCommand().cmdloop()