#!/usr/bin/python3
def print_fast_alpha(i):
    if i <= 90:
        print(chr(i), end="")
        i += 1
        print_fast_alpha(i)
    else:
        print()
