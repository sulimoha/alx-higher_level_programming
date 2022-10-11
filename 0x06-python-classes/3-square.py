#!/usr/bin/python3
"""Area of a square"""


class Square:
    """a class Square that defines a square"""
    def __init__(self, size=0):
        """Instantiation with optional size"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = int(size)

    def area(self):
        """ returns the current square area"""
        return self.__size ** 2
