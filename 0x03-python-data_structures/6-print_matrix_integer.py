#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        noSpace = True
        for column in row:
            if noSpace is False:
                print(" ", end="")
            else:
                noSpace = False
            print("{:d}".format(column), end="")
        print()
