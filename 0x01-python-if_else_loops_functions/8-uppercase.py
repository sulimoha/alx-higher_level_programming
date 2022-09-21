#!/usr/bin/python3
def uppercase(str):
    for c in (str):
        t = ord(c)
        if t >= 97 and t <= 122:
            t = chr(t - 32)
        else:
            t = c
        print("{:s}".format(t), end="")
    print("")
