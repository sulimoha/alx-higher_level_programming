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

        self.size = size
        self.position = position

    @property
    def size(self):
        """size getter
            Return:
                Size of square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """size setter
            Args:
                value (int): size
            Raises
                TypeError: if size is not int
                ValueError: if size < 0
            Returns:
                None
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """position getter"""
        return self.__position

    @position.setter
    def position(self, value):
        """position setter
            Args:
                value (tuple): position of the square in 2D space
            Returns:
                None
        """
        if len(value) != 2 or type(value) != tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) != int or value[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[1]) != int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """ returns the current square area (int)"""
        return self.__size ** 2

    def my_print(self):
        """prints in stdout the square with the character #"""
        if self.__size == 0:
            print()
        else:
            print("\n" * self.__position[1], end="")
            for i in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)

    def __str__(self):
        """
        defining printing behavior of the class
        """
        if self.__size == 0:
            return ''
        new_lines = '\n' * self.position[1]
        spaces = ' ' * self.position[0]
        hashes = '#' * self.size
        return new_lines + '\n'.join(spaces + hashes for e in range(self.size))
