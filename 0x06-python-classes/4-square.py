#!/usr/bin/python3
'''Square class definition'''


class Square:
    '''A square

    Attributes:
        __size (int): size of a side of a square
    '''
    def __init__(self, size=0):
        '''Initialize a square instance

        Args:
            size (int): size of the sides of a square

        Returns: None
        '''
        self.size = size

    def area(self):
        '''calculates the area of the square

        Returns:
            Area of the square
        '''
        return(self.__size ** 2)

    @property
    def size(self)
        '''getter of size

        Returns:
            size of the square
        '''
        return(self.__size)

    @size.setter
    def size(self, value):
        '''setter of value

        Args:
            value (int): the size of the square

        Returns:
            None
        '''
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
