#!/usr/bin/python3

"""This module contain a base class"""
from fileinput import filename
import json

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

        if not list:
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
        name = cls.__name__ + ".json"
        list_dict = []
        for obj in list_objs:
            list_dict.append(obj.to_dictionary())
        with open(name, 'w') as f:
            if not list_objs:
                f.write()
            else:
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
