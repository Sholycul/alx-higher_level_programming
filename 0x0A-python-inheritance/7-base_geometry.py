#!/usr/bin/python3

"""
Module for Base Geometry based on `6-base_geometry`
Public instance method: def area(self):
that raises an Exception with the message area() is not implemented
Public instance method: def integer_validator(self, name, value):
that validates value:
If value is not an integer: raise a TypeError exception,
with the message <name> must be an integer
if value is less or equal to 0: raise a ValueError exception
with the message <name> must be greater than 0
"""
class BaseGeometry:
    def area(self):
        """
        Raises:
            Exception: Always raises an exception with the message "area() is not implemented".
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates if the value is an integer and greater than 0.

        Args:
            name (str): Name of the value.
            value (int): Value to be validated.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

