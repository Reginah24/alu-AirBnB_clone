
#!/usr/bin/python3
"""Command line interpreter for AirBnB clone"""

import cmd
import models


class HBNBCommand(cmd.Cmd):
    """Class for the console, inheriting from cmd.Cmd"""
    prompt = '(hbnb)'

    def do_quit(self, arg):
        """Exit the program."""
        return True

    def do_EOF(self, arg):
        """Exit the program with EOF (Ctrl+D)."""
        return True

    def emptyline(self):
        """Do nothing on an empty line."""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel or other class."""
        if not arg:
            print("** class name missing **")
            return
        if arg not in models.dict_classes:
            print("** class doesn't exist **")
            return
        instance = models.dict_classes[arg]()
        instance.save()
        print(instance.id)

    def do_show(self, arg):
        """Shows the string representation of an instance."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in models.dict_classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_key = args[0] + "." + args[1]
        if instance_key in models.storage.all():
            print(models.storage.all()[instance_key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in models.dict_classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_key = args[0] + "." + args[1]
        if instance_key in models.storage.all():
            del models.storage.all()[instance_key]
            models.storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """Shows all instances, or all instances of a class."""
        args = arg.split()
        if not arg:
            for value in models.storage.all().values():
                print(str(value))
        elif args[0] not in models.dict_classes:
            print("** class doesn't exist **")
        else:
            for key, value in models.storage.all().items():
                if key.split('.')[0] == args[0]:
                    print(str(value))

    def do_update(self, arg):
        """Updates an instance based on class name and id."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in models.dict_classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        instance_key = args[0] + "." + args[1]
        if instance_key in models.storage.all():
            attr_name = args[2]
            attr_value = args[3].strip('"')
            setattr(models.storage.all()[instance_key], attr_name, attr_value)
            models.storage.save()
        else:
            print("** no instance found **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()