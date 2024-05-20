#!/usr/bin/python3
"""
Module 2-matrix_divided
Contains a function that divides all elements of a matrix
"""

def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a divisor.

    Args:
        matrix (list of list of int/float): The matrix to be divided.
        div (int/float): The divisor.

    Returns:
        list of list of float: A new matrix with all elements divided by div,
                               rounded to 2 decimal places.

    Raises:
        TypeError: If matrix elements are not lists of int/float,
                   if rows are not the same size, or if div is not a number.
        ZeroDivisionError: If div is zero.
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
    
    if not all(isinstance(el, (int, float)) for row in matrix for el in row):
        raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
    
    row_length = len(matrix[0])
    if not all(len(row) == row_length for row in matrix):
        raise TypeError('Each row of the matrix must have the same size')
    
    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')
    
    if div == 0:
        raise ZeroDivisionError('division by zero')
    
    return [[round(el / div, 2) for el in row] for row in matrix]

