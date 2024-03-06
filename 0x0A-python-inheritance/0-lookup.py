#!/usr/bin/python3

def lookup(obj):
    """Returns a list of available attributes and methods of an object."""
    return ([attr for attr in dir(obj)])
