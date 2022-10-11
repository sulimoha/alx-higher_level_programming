#!/usr/bin/python3
"""2. Size validation"""


class Square:
    """ a class Square that defines a square by: (based on 1-square.py)"""
    def __init__(self, size=0):
        """Instantiation with optional size"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = int(size)
