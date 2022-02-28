#!/usr/bin/python3
'''A Rectangle class'''


Base = __import__('base').Base


class Rectangle(Base):
    ''' A rectangle class '''
    def __init__(self, width, height, x=0, y=0, id=None):
        ''' initialize the rectangle '''
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        ''' returning private attribute '''
        return self.__width

    @width.setter
    def width(self, value):
        ''' setting private attribute '''
        self.__width = value

    @property
    def height(self):
        ''' returning private attribute '''
        return self.__height

    @height.setter
    def height(self, value):
        ''' setting private attribute '''
        self.__height = value

    @property
    def x(self):
        ''' returning private attribute '''
        return self.__x

    @x.setter
    def x(self, value):
        ''' setting private attribute '''
        self.__x = value

    @property
    def y(self):
        ''' returning private attribute '''
        return self.__y

    @x.setter
    def y(self, value):
        ''' setting private attribute '''
        self.__y = value
