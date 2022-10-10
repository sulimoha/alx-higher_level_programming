#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    j = 0
    try:
        for i in my_list:
            if (i <= x):
                print(i, end="")
                j += 1
        print()
    except IndexError:
        print("index {} doesn't exist".format(x))
    return j
