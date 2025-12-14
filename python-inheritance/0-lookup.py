#!/usr/bin/python3
"""
Module that defines a function to list available attributes and methods of an object
"""

def lookup(obj):
    """
    Returns the list of available attributes and methods of an object

    Args:
        obj: any Python object

    Returns:
        list: list of attributes and methods
    """
    return dir(obj)
