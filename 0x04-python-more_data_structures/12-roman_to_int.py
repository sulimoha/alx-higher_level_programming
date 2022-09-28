#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_dictionary = {"I": 1, "IV": 4, "V": 5, "IX": 9, "X": 10, "XL": 40,
                        "L": 50, "XC": 90, "C": 100, "CD": 400, "D": 500,
                        "CM": 900, "M": 1000}
    if roman_string.isalpha() is False or roman_string is None:
        return 0
    sum = 0
    for k, v in roman_dictionary.items():
        if roman_string.upper() == k:
            return v
        for char in roman_string.upper():
            if char == k:
                sum = sum + v
    return sum
