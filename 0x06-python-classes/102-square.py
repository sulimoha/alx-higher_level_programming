#!/usr/bin/python3
"""Access and update private attribute"""


class Square:
    """a class Square that defines a square"""
    def __init__(self, size=0):
        """Instantiation with optional size"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def size(self):
        """size getter"""
        return self.__size

    @size.setter
    def size(self, value):
        """size setter"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """ returns the current square area"""
        return self.__size ** 2

    def __eq__(self, other):
        """check if equal to another square"""
        return(self.area() == other.area())

    def __lt__(self, other):
        """check if less than other square"""
        return(self.area() < other.area())

    def __le__(self, other):
        """check if less than or equal to other square"""
        return(self.area() <= other.area())

    def __ne__(self, other):
        """check if not equal to another suqare"""
        return(self.area() != other.area())

    def __gt__(self, other):
        """check if greater than another square"""
        return(self.area() > other.area())

    def __ge__(self, other):
        """check if greater than or equal to another square"""
        return(self.area() >= other.area())
