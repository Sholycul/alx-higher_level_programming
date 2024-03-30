#!/usr/bin/python3

"""
BaseGeometry Module
Defines a class BaseGeometry representing base geometry.
"""


class BaseGeometry:
    """
    BaseGeometry class representing base geometry.
    """

    def area(self):
        """
        Computes the area of the geometry.

        Raises:
            Exception: If the method is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates the value.

        Args:
            name (str): The name of the value.
            value (int): The value to be validated.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

