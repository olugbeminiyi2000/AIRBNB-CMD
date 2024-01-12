#!/usr/bin/python3

if __name__ == "__main__":
  from datetime import datetime
  from models.base_model import BaseModel
  from models.user import User
  from models.state import State
  from models.city import City
  from models.amenity import Amenity
  from models.place import Place
  from models.review import Review
  from models import storage
  import ast
  import cmd
  import copy
  import sys

  class HBNBCommand(cmd.Cmd):
    HBNBClasses = [
        "BaseModel", "User", "State", "City", "Amenity", "Place", "Review"
    ]
    prompt = "(hbnb) "

    def do_update(self, args):
      """
      Updates an instance based on the class name and id 
      by adding or updating attribute (save the change into the JSON file).
      Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com".

      Usage: update <class name> <id> <attribute name> "<attribute value>"
      Only one attribute can be updated at the time!!!
      You can assume the attribute name is valid (exists for this model)
      The attribute value must be casted to the attribute type!!!

      id, created_at and updated_at cant’ be updated.
      You can assume they won’t be passed in the update command
      Only “simple” arguments can be updated: string, integer and float.
      You can assume nobody will try to update list of ids or datetime.
      """
      list_args = args.split()
      if len(list_args) < 1:
        print("** class name missing **")
      else:
        if list_args[0] in self.HBNBClasses:
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
      """
      Prints all string representation of all instances
      based or not on the class name.
      Ex: $ all BaseModel or $ all.
      """
      if arg == "":
        print("** class name missing **")
      else:
        if arg in self.HBNBClasses or arg == ".":
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
      Ex: $ create BaseModel
      """
      if arg == "":
        print("** class name missing **")
      else:
        if arg == "BaseModel":
          model = BaseModel()
          model.save()
          print(model.id)
          storage.reload()
        elif arg == "User":
          model = User()
          model.save()
          print(model.id)
          storage.reload()
        elif arg == "State":
          model = State()
          model.save()
          print(model.id)
          storage.reload()
        elif arg == "City":
          model = City()
          model.save()
          print(model.id)
          storage.reload()
        elif arg == "Amenity":
          model = Amenity()
          model.save()
          print(model.id)
          storage.reload()
        elif arg == "Place":
          model = Place()
          model.save()
          print(model.id)
          storage.reload()
        elif arg == "Review":
          model = Review()
          model.save()
          print(model.id)
          storage.reload()
        else:
          print("** class doesn't exist **")

    def do_destroy(self, args):
      """
      Deletes an instance based on the class name
      and id (save the change into the JSON file).
      Ex: $ destroy BaseModel 1234-1234-1234.
      """
      list_args = args.split()
      if len(list_args) < 1:
        print("** class name missing **")
      else:
        if list_args[0] in self.HBNBClasses:
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
      Ex: $ show BaseModel 1234-1234-1234.
      """
      list_args = args.split()
      if len(list_args) < 1:
        print("** class name missing **")
      else:
        if list_args[0] in self.HBNBClasses:
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
