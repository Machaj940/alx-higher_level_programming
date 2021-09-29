#!/usr/bin/python3
'''square class definition'''


class square:
    '''A square

    Attributes:
        __size (int): size of a side of a square
    '''
    def __init__(self, size):
        '''initialize a square instance

        Args:
            size (int): size of the sides of a square

        Returns: None
        '''
        self.__size = size
