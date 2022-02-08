#!/usr/bin/python3
"""Module that adds 2 integers"""

def add_integer(a, b=98):
    """adds 2 integers"""
    if type(a) == float:
        a = int(a)
    if type(b) == float:
        b = int(b)
    if type(a) != int and type(a) != float:
        raise TypeError('a must be an integer')
    if type(b) != int and type (b) != float:
        raise TypeError('b must be an integer')
    return (a + b)
