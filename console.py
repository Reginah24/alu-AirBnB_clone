#!/usr/bin/python3
"""Command interpreter for AirBnB clone project."""
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

classes = {
    'BaseModel': BaseModel,
    'User': User,
    'State': State,
    'City': City,
    'Amenity': Amenity,
    'Place': Place,
    'Review': Review
}

class HBNBCommand(cmd.Cmd):
    """Command processor for the AirBnB clone."""
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF to exit the program."""
        print()
        return True

    def emptyline(self):
        pass

    def do_create(self, arg):
        """Creates a new instance of a class, saves it, and prints the id."""
        if not arg:
            print("** class name missing **")
            return
        if arg not in classes:
            print("** class doesn't exist **")
            return
        obj = classes[arg]()
        obj.save()
        print(obj.id)

    def do_show(self, arg):
        """Prints the string representation of an instance based on class name and id."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        objs = storage.all()
        if key not in objs:
            print("** no instance found **")
            return
        print(objs[key])

    def do_destroy(self, arg):
        """Deletes an instance based on class name and id."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        objs = storage.all()
        if key not in objs:
            print("** no instance found **")
            return
        del objs[key]
        storage.save()

    def do_all(self, arg):
        """Prints all string representations of all instances or of a class."""
        objs = storage.all()
        if arg and arg not in classes:
            print("** class doesn't exist **")
            return
        result = []
        for obj in objs.values():
            if not arg or obj.__class__.__name__ == arg:
                result.append(str(obj))
        print(result)

    def do_update(self, arg):
        """Updates an instance based on class name and id by adding or updating attribute."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        objs = storage.all()
        if key not in objs:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        attr_name = args[2]
        attr_value = args[3].strip('"')
        obj = objs[key]
        try:
            casted_value = eval(attr_value)
        except:
            casted_value = attr_value
        setattr(obj, attr_name, casted_value)
        obj.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
