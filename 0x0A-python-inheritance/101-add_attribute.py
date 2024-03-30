#!/usr/bin/python3

"""
a function that adds a new attribute to an object if it’s possible:

Raise a TypeError exception, with the message can't add new attribute if the object can’t have new attribute
You are not allowed to use try/except
You are not allowed to import any module
"""

def add_attribute(obj, name, value):
    """
    Adds a new attribute to an object if possible.

    Args:
        obj: Object to which the attribute will be added.
        name (str): Name of the attribute.
        value: Value of the attribute.

    Raises:
        TypeError: If the object cannot have new attributes.
    """
    if not hasattr(obj, '__dict__') and not hasattr(type(obj), '__slots__'):
        raise TypeError("can't add new attribute")

    setattr(obj, name, value)
