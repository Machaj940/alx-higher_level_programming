#!/usr/bin/python3
'''Base class for Python Almost-a-Circle project'''


class Base:
    '''This class will be the base of all other classes in the project'''
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
