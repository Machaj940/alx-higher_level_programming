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
        return(self.__size * self.__size)

    @property
    def size(self):
        '''getter of __size

        Returns:
            size of the square
        '''
        return(self.__size)

    @size.setter
    def size(self, value):
        '''setter of __size

        Args:
            value (int): the size of the square

        Returns:
            None
        '''
        if type(value) is not int and type(value) is not float:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    
    def __lt__(self, other):
        '''
            less than <
        '''
        return(self.area() < other.area())

    def __le__(self, other):
        '''
            less or equal than <=
        '''
        return(self.area() <= other.area())

    def __eq__(self, other):
        '''
            equal to ==
        '''
        return(self.area() == other.area())

    def __ge__(self, other):
        '''
            greater or equal than >=
        '''
        return(self.area() >= other.area())

    def __gt__(self, other):
        '''
            greater than >
        '''
        return(self.area() > other.area())

    def __ne__(self, other):
        '''
            not equal !=
        '''
        return(self.area() != other.area())
