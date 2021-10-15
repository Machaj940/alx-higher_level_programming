#!/usr/bin/python3
'''Square class definition'''


class Square:
    '''A square

    Attributes:
        __size (int): size of a side of a square
    '''
    def __init__(self, size=0, position=(0, 0)):
        '''Initialize a square instance

        Args:
            size (int): size of the sides of a square

        Returns: None
        '''
        self.size = size
        self.position = position

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

    def my_print(self):
        '''
            prints the square
        '''
        if self.__size == 0:
            print()
            return
        for col in range(self.__size):
            for row in range(self.size):
                print("#", end="")
            print()

    @property
    def position(self):
        '''getter of __position

        Return:
            the position of the square in 2D
        '''
        return(self.__position)

    @position.setter
    def position(self, value):
        '''setter of __position

        Args:
            value(tuple): position of the square in 2D
        Returns:
            None
        '''
        if type(value) is not tuple or len(value) != 2 or \
           type(value[0]) is not int or value[0] < 0 or \
           type(value[1]) is not int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
