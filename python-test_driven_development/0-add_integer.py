#!/usr/bin/python3
"""
Module 0-add_integer
Contains a function that adds two integers or floats casted to integers.
"""

def add_integer(a, b=98):
    """
    Adds two integers or floats casted to integers.

    Args:
        a (int, float): First number.
        b (int, float): Second number, defaults to 98.

    Returns:
        int: The integer addition of a and b.

    Raises:
        TypeError: If a or b are not integers or floats.
    """
    if not isinstance(a, (int, float)):
        raise TypeError('a must be an integer')
    if not isinstance(b, (int, float)):
        raise TypeError('b must be an integer')
    return int(a) + int(b)

