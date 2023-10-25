#!/usr/bin/python3
""" Module that have the class Base
"""

from models.base import Base


class Rectangle(Base):
    """class Rectangle
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """function that return the area
        """
        return (self.__height * self.__width)

    def display(self):
        """function that print the rectangle with "#"
        x = spaces in before de width
        y = line breaks before the print the rectangle
        """
        print("\n" * self.__y, end="")
        for col in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """Magic method str,
        print the actual size of the rectangle.
        """
        s = "[Rectangle]"
        size = f"{self.x}/{self.y}"
        return f"{s} ({self.id}) {size} - {self.width}/{self.height}"

    def update(self, *args, **kwargs):
        """update the args of the class Rectangle,
        1st argument should be the id attribute
        2nd argument should be the width attribute
        3rd argument should be the height attribute
        4th argument should be the x attribute
        5th argument should be the y attribute
        """
        names = ["id", "width", "height", "x", "y"]
        if args is not () and args is not None:
            for value, name in zip(args, names):
                setattr(self, name, value)
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """public method, that returns the dictionary
        representation of a Rectangle.
        """
        new_dic = {
                "width": self.width,
                "height": self.height,
                "x": self.x,
                "y": self.y,
                "id": self.id
                }

        return new_dic
