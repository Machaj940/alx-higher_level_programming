#!/usr/bin/python3
"""Square class definition"""


class Square:
    """A square

    Attributes:
        __size (int): size of a side of a square
    """
    def __init__(self, size=0):
        """Initialize a square instance

        Args:
            size (int): size of the sides of a square

        Returns: None
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

# OR

#class Square:
#    '''A class square'''
#    def __init__(self, size=0):
#       if isinstance(size, int):
#            self.__size = size
#        else:
#            raise TypeError("size must be an integer")
#        if size >= 0:
#            self.__size = size
#        else:
#            raise ValueError("size must be >= 0")
