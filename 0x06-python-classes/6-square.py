#!/usr/bin/python3
""" Printing a square"""


class Square:
    """a class Square that defines a square
        Attributes:
            size (int): Size of square
            position (tuple): position of space and lines
    """
    def __init__(self, size=0, position=(0, 0)):
        """Instantiation
            Args:
                size(int): size
                position(tuple): position
            Returns:
                None
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
        if type(position[0]) != int or type(position[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

    @property
    def size(self):
        """size getter"""
        return self.__size

    @property
    def position(self):
        """position getter"""
        return self.__position

    @size.setter
    def size(self, value):
        """size setter"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @position.setter
    def position(self, value):
        """position setter"""
        if type(value[0]) != int or type(value[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """ returns the current square area"""
        return self.__size ** 2

    def my_print(self):
        """prints in stdout the square with the character #"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                if(self.__position[1] <= 1):
                    for k in range(self.__position[0]):
                        print('_', end="")
                for j in range(self.__size):
                    print('#', end="")
                print()
