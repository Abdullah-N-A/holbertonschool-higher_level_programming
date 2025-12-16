#!/usr/bin/python3
"""
Module that defines a function to check if an object
is an instance of a class or a class that inherited from it.
"""

def is_kind_of_class(obj, a_class):
    """
    Returns True if the object is an instance of, or if the object
    is an instance of a class that inherited from, the specified class.
    Otherwise returns False.
    """
    return isinstance(obj, a_class)