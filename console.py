#!/usr/bin/python3

if __name__ == "__main__":
  from datetime import datetime
  from models.base_model import BaseModel
  from models import storage
  import ast
  import cmd
  import copy
  import sys

  class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_update(self, args):
      list_args = args.split()
      if len(list_args) < 1:
        print("** class name missing **")
      else:
        if list_args[0] == "BaseModel":
          if len(list_args) > 1:
            key = f"{list_args[0]}.{list_args[1]}"
            storage.reload()
            change__objects_dict = storage.all()
            if key in change__objects_dict:
              if len(list_args) > 2:
                if len(list_args) > 3:
                  attribute_name = list_args[2]
                  attribute_value = str(ast.literal_eval(list_args[3]))
                  try:
                    if isinstance(change__objects_dict[key][attribute_name],
                                  int):
                      attribute_value = int(attribute_value)
                      change__objects_dict[key][
                          attribute_name] = attribute_value
                    elif isinstance(change__objects_dict[key][attribute_name],
                                    float):
                      attribute_value = float(attribute_value)
                      change__objects_dict[key][
                          attribute_name] = attribute_value
                    else:
                      change__objects_dict[key][
                          attribute_name] = attribute_value
                  except KeyError:
                    try:
                      if isinstance(int(attribute_value), int):
                        change__objects_dict[key][attribute_name] = int(
                            attribute_value)
                    except ValueError:
                      try:
                        if isinstance(float(attribute_value), float):
                          change__objects_dict[key][attribute_name] = float(
                              attribute_value)
                      except ValueError:
                        change__objects_dict[key][
                            attribute_name] = attribute_value
                  storage.save()
                else:
                  print("** value missing **")
              else:
                print("** attribute name missing **")
            else:
              print("** no instance found **")
          else:
            print("** instance id missing **")
        else:
          print("** class doesn't exist **")

    def do_all(self, arg):
      if arg == "":
        print("** class name missing **")
      else:
        if arg == "BaseModel":
          storage.reload()
          display_all_list = []
          temp_show_dict = copy.deepcopy(storage.all())
          for key in list(temp_show_dict):
            base_class = temp_show_dict[key]["__class__"]
            del temp_show_dict[key]["__class__"]
            display_all_list.append(
                f"[{base_class}] ({temp_show_dict[key]['id']}) {temp_show_dict[key]}"
            )
          print(display_all_list)
        else:
          print("** class doesn't exist **")

    def do_create(self, arg):
      """
      Creates a new instance of BaseModel, 
      saves it (to the JSON file) and prints the id
      """
      if arg == "":
        print("** class name missing **")
      else:
        if arg == "BaseModel":
          model = BaseModel()
          model.save()
          print(model.id)
          storage.reload()
        else:
          print("** class doesn't exist **")

    def do_destroy(self, args):
      """
      Deletes an instance based on the class name
      and id (save the change into the JSON file). 
      """
      list_args = args.split()
      if len(list_args) < 1:
        print("** class name missing **")
      else:
        if list_args[0] == "BaseModel":
          if len(list_args) > 1:
            key = f"{list_args[0]}.{list_args[1]}"
            storage.reload()
            change__objects_dict = storage.all()
            if key in change__objects_dict:
              del change__objects_dict[key]
              storage.save()
            else:
              print("** no instance found **")
          else:
            print("** instance id missing **")
        else:
          print("** class doesn't exist **")

    def do_show(self, args):
      """
      Prints the string representation of an 
      instance based on the class name and id
      """
      list_args = args.split()
      if len(list_args) < 1:
        print("** class name missing **")
      else:
        if list_args[0] == "BaseModel":
          if len(list_args) > 1:
            key = f"{list_args[0]}.{list_args[1]}"
            storage.reload()
            temp_show_dict = copy.deepcopy(storage.all())
            if key in temp_show_dict:
              base_class = temp_show_dict[key]["__class__"]
              del temp_show_dict[key]["__class__"]
              print(
                  f"[{base_class}] ({temp_show_dict[key]['id']}) {temp_show_dict[key]}"
              )
            else:
              print("** no instance found **")
          else:
            print("** instance id missing **")
        else:
          print("** class doesn't exist **")

    def do_quit(self, arg):
      """Quit command to exit the program"""
      return True

    def do_EOF(self, arg):
      """EOF command to exit the program if EOF is reached"""
      if arg == "\n":
        print("")
      return True

    def emptyline(self):
      pass

    def preloop(self):
      if sys.stdin.isatty():
        return
      self.stdin = sys.stdin
      try:
        while True:
          line = input("(hbnb) ")
          print("")
          line = self.precmd(line)
          stop = self.onecmd(line)
          stop = self.postcmd(stop, line)
      except EOFError:
        self.do_EOF("\n")

  HBNBCommand().cmdloop()
