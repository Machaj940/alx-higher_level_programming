#!/usr/bin/python3
"""Inherits from class REctangle"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """inherits from class Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """initialize instance attributes"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Print the square details"""
        return (
            f"[{self.__class__.__name__}] ({self.id}) {self.x}/{self.y} - "
            f"{self.size}"
        )

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        if len(args) == 0:
            for key, val in kwargs.items():
                self.__setattr__(key, val)
            return

        try:
            self.id = args[0]
            self.size = args[1]
            self.x = args[2]
            self.y = args[3]
        except IndexError:
            pass
