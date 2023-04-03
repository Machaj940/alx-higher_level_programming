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
