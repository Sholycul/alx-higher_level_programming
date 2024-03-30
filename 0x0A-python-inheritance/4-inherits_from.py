#!/usr/bin/python3

"""
inherits_from Module
Creates a function that returns true
if object is an instance of a class that inherited
(directly or indirectly) from the specified class.
"""

def inherits_from(obj, a_class):
    """
    Checks if an object is an instance of a class that inherited from a specified class.

    Args:
        obj: The object to check.
        a_class: The specified class.

    Returns:
        True if obj is an instance of a class that inherited from a_class; otherwise False.
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
