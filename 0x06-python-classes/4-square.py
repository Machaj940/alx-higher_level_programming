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
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value


# OR

#class Square:
#    '''A class square'''
#    def __init__(self, size=0):
#       self.size = size

#    @property
#    def size(self):
#        return self.__size

#    @size.setter
#    def size(self, value):
#	if isinstance(value, int):
#            self.__size = value
#	else:
#            raise TypeError("size must be an integer")
#	if value >= 0:
#            self.__size = value
#        else:
#            raise ValueError("size must be >= 0")

#    def area(self):
#        return self.__size * self.__size
