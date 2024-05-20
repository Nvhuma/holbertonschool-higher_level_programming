#!/usr/bin/python3
"""
Module 0-add_integer
Contains a function that adds two integers
"""

def add_integer(a, b=98):
    """
    Adds two integers or floats casted to integers

    Args:
        a: first integer
        b: second integer, defaults to 98

    Returns:
        The integer addition of a and b

    Raises:
        TypeError: if a or b are not integers or floats
    """
    if not isinstance(a, (int, float)):
        raise TypeError('a must be an integer')
    if not isinstance(b, (int, float)):
        raise TypeError('b must be an integer')
    return int(a) + int(b)

