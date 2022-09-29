#!/usr/bin/python3
def roman_to_int(roman_string):
    if (roman_string is None) or isinstance(roman_string, str) is False:
        return 0
    roman_letters = [
        ['I', 1], ['V', 5], ['X', 10], ['L', 50], ['C', 100],
        ['D', 500], ['M', 1000]
    ]
    num = 0
    last = 0
    for letter in roman_string:
        for elem in roman_letters:
            if letter == elem[0]:
                if last == 0 or last >= elem[1]:
                    num += elem[1]
                elif last < elem[1]:
                    num += elem[1] - (last * 2)
                last = elem[1]
    return num
