#!/usr/bin/python3
'''Define a class Rectangle'''


class Rectangle:
    '''Create a rectangle'''
    def __init__(self, width=0, height=0):
        '''initializes the rectangle'''
        self.width = width
        self.height = height

    @property
    def width(self):
        '''getter for the private instance attribute width'''
        return(self.__width)

    @width.setter
    def width(self, value):
        '''setter for the private instance attribute width'''
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        '''getter for the private instance attribute height'''
        return(self.__height)

    @height.setter
    def height(self, value):
        '''setter for the private instance attribute height'''
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        '''return the area of the rectangle'''
        return(self.__width * self.__height)

    def perimeter(self):
        '''returns the perimeter of the rectangle'''
        if self.__width == 0 or self.__height == 0:
            return(0)
        return((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        '''print rectangle'''
        rec = ""
        for i in range(0, self.__height):
            for j in range(0, self.__width):
                rec += '#'
            rec += '\n'
        return(rec.strip('\n'))

    def __repr__(self):
        '''returns a string representatiion of the rectangle'''
        return("Rectangle({:d}, {:d})".format(self.__width, self.__height))
    # or
    # return f"Rectangle({self.__width}, {self.__height})"
    # or
    # return "Rectangle(" + str(self.__width) + ", " + str(self.__height) + ")"
