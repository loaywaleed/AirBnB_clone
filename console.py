#!/usr/bin/python3
"""Console interpreter"""
import cmd
from models.base_model import BaseModel
from models import storage
import re


class HBNBCommand(cmd.Cmd):
    """A class that implements a command interpreter"""
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print()
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered"""
        pass

    def do_create(self, arg):
        """Creates an instance.
        """
        if arg == "" or arg is None:
            print("** class name missing **")
        elif arg not in storage.classes():
            print("** class doesn't exist **")
        else:
            b = storage.classes()[arg]()
            b.save()
            print(b.id)

    def do_show(self, arg):
        args = arg.split()
        if arg == "" or arg is None:
            print("** class name missing **")
        elif args[0] not in storage.classes():
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = f"{args[0]}.{args[1]}"
            if key not in storage.all():
                print("** no instance found **")
            else:
                print(storage.all()[key])

    def do_destroy(self, arg):
        args = arg.split()
        if arg == "" or arg is None:
            print("** class name missing **")
        elif args[0] not in storage.classes():
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = f"{args[0]}.{args[1]}"
            if key not in storage.all():
                print("** no instance found **")
            else:
                del(storage.all()[key])
                storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances.
        """
        if arg != "":
            words = arg.split(' ')
            if words[0] not in storage.classes():
                print("** class doesn't exist **")
            else:
                np = [str(obj) for key, obj in storage.all().items()
                      if type(obj).__name__ == words[0]]
                print(np)
        else:
            new_list = [str(obj) for key, obj in storage.all().items()]
            print(new_list)

    def do_update(self, arg):
        """Updates an instance by adding or updating attribute.
        """
        if arg == "" or arg is None:
            print("** class name missing **")
            return

        rex = r'^(\S+)(?:\s(\S+)(?:\s(\S+)(?:\s((?:"[^"]*")|(?:(\S)+)))?)?)?'
        match = re.search(rex, arg)
        classname = match.group(1)
        uid = match.group(2)
        attribute = match.group(3)
        value = match.group(4)
        if not match:
            print("** class name missing **")
        elif classname not in storage.classes():
            print("** class doesn't exist **")
        elif uid is None:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(classname, uid)
            if key not in storage.all():
                print("** no instance found **")
            elif not attribute:
                print("** attribute name missing **")
            elif not value:
                print("** value missing **")
            else:
                cast = None
                if not re.search('^".*"$', value):
                    if '.' in value:
                        cast = float
                    else:
                        cast = int
                else:
                    value = value.replace('"', '')
                attributes = storage.attributes()[classname]
                if attribute in attributes:
                    value = attributes[attribute](value)
                elif cast:
                    try:
                        value = cast(value)
                    except ValueError:
                        pass  # fine, stay a string then
                setattr(storage.all()[key], attribute, value)
                storage.all()[key].save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
