#!/usr/bin/python3
'''Base class for Python Almost-a-Circle project'''


import json


class Base:
    '''This class will be the base of all other classes in the project'''
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """return json representation of list_dictionaries"""
        if list_dictionaries is None or list_dictionaries == []:
            return f"[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        if list_objs is None:
            list_objs = []
        listofDictionaries = list(map(cls.to_dictionary, list_objs))
        dictlist_to_json = cls.to_json_string(listofDictionaries)
        with open(f"{cls.__name__}.json", mode="w",
                  encoding="utf-8") as f:
            f.write(dictlist_to_json)

#            OR
#            json.dump(listofDictionaries, f)
#            you do not need to do the dictlist_to_json... step like above

    @staticmethod
    def from_json_string(json_string):
        """convert json string to list"""
        if json_string is None:
            return list()
        return json.loads(json_string)
