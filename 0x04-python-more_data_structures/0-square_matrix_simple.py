#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in range(len(matrix)):
        new_matrix.append(list(map(lambda x: (x ** 2), matrix[row])))
    return new_matrix
