#!/usr/bin/python3

"""This module contain a base class"""
import json
import csv


class Base:
    """ A base class """
    __nb_objects = 0

    def __init__(self, id=None) -> None:
        """ Run when a new instance is created """
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns a json representation of the input"""

        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """ returns the list of the JSON string representation """

        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """ write the JSON string representation of list_objs to a file """
        filename = cls.__name__ + ".json"
        list_dict = []
        for obj in list_objs:
            list_dict.append(obj.to_dictionary())
        with open(filename, 'w') as f:
                f.write(cls.to_json_string(list_dict))

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with all attributes already set """
        instance = cls(1, 1, id=10000)
        instance.update(**dictionary)

        return instance

    @classmethod
    def load_from_file(cls):
        """  returns a list of instances """
        filename = cls.__name__ + ".json"
        obj_list = []
        try:
            with open(filename, "r") as f:
                json_string = f.read()
                for obj_dict in cls.from_json_string(json_string):
                    obj = cls.create(**obj_dict)
                    obj_list.append(obj)
        except FileNotFoundError:
            return []

        return obj_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ write the CSV string representation of list_objs to a file """
        filename = "{}.csv".format(cls.__name__)
        list_csv = []
        for obj in list_objs:
            if cls.__name__ == "Rectangle":
                obj_list = [obj.id, obj.width, obj.height, obj.x, obj.y]
            elif cls.__name__ == "Square":
                obj_list = [obj.id, obj.size, obj.x, obj.y]
            list_csv.append(obj_list)

        with open(filename, "w", newline="") as f:
            csvwriter = csv.writer(f)
            for line in list_csv:
                csvwriter.writerow(line)

    @classmethod
    def load_from_file_csv(cls):
        """  returns a list of instances fro CSV file """
        filename = "{}.csv".format(cls.__name__)

        try:
            with open(filename, "r") as f:
                list_csv = csv.reader(f)
                args_list = []
                obj_list = []
                for line in list_csv:
                    if cls.__name__ == "Rectangle":
                        obj_dict = {"id": int(line[0]), "width": int(line[1]),
                                    "height": int(line[2]), "x": int(line[3]),
                                    "y": int(line[4])}
                    elif cls.__name__ == "Square":
                        obj_dict = {"id": int(line[0]), "size": int(line[1]),
                                    "x": int(line[2]), "y": int(line[3])}
                    args_list.append(obj_dict)

                for args in args_list:
                    new_obj = cls.create(**args)
                    obj_list.append(new_obj)

                return obj_list
        except Exception:
            return []
