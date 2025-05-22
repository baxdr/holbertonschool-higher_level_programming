#!/usr/bin/python3
"""
This module defines a Square class with encapsulated size, position,
and area computation, as well as the ability to print the square with
positions.
"""


class Square:
    """
    Represents a square with size and position encapsulation, area calculation,
    and a method to print the square at a given position.

    Attributes:
        __size (int): The size of the square (private).
        __position (tuple): A tuple of 2 positive integers representing
                             the position of the square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new Square instance with a given size and position.

        Args:
            size (int): The size of the square (default is 0).
            position (tuple): The position(x, y)of the square(default is(0,0)

        Raises:
            TypeError:If size is not an int or position is not tuple of 2+int
            ValueError:If size is less than 0 or position contains non-+ int
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Retrieves the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square with validation.

        Args:
            value (int): The new size value.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Retrieves the position of the square.

        Returns:
            tuple: The position of the square (x, y).
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the position of the square with validation.

        Args:
            value (tuple): The new position (x, y).

        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
            ValueError: If any element of value is less than or equal to 0.
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(i, int) and i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square using the '#' character, considering the position.
        If size is 0,prints an empty line.
        Returns:
            None
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):  # Print leading spaces y-coor
                print()
            for _ in range(self.__size):  # Print each row of the square
                print(" " * self.__position[0] + "#" * self.__size)
