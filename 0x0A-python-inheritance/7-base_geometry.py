#!/usr/bin/python3
'''Create an class BaseGeometry'''


class BaseGeometry:
    '''a class'''
    def area(self):
        '''raise an exception'''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''validates that value is an int greater than 0'''
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
