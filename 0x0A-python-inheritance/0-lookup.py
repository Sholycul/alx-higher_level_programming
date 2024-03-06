#!usr/bin/python3
"""A function file that defines available attributes and method"""

def lookup(obj):
    """Returns available attributes as a list"""
    return (dir(obj))
