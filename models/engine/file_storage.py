#!/usr/bin/python3
"""
class that serializes an instance and
deserialize and instance
Purpose: to perform persistence of data
"""

import json


class FileStorage:
    """ class to serialize/deserialize class instance to JSON """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns the dictionary __objects """
        return self.__objects

    def new(self, obj):
        """ sets __obj with key - classname.id in objects """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """ serialise the dict """
        dict = {}
        for key, val in self.__objects.items():
            dict[key] = val.to_dict()

        dict_str = json.dumps(dict)

        with open(self.__file_path, "w") as f:
            f.write(dict_str)

    def reload(self):
        """ deserialise the json string """
        try:
            with open(self.__file_path, "r") as f:
                my_dict = json.load(f)
            for key, val in my_dict.items():
                self.__objects[key] = val
        except FileNotFoundError:
            pass
