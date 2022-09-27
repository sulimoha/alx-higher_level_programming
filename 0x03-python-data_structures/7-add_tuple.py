#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    temp = (tuple_a, tuple_b)
    j = 0
    a = j
    b = j
    for sum in temp:
        for count in sum:
            if j == 0:
                a = a + count
            elif j == 1:
                b = b + count
            else:
                break
            j = j + 1
        j = 0
    sum = (a, b)
    return sum
