#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_dictionary = {"I": 1, "IV": 4, "V": 5, "IX": 9, "X": 10, "XL": 40,
                        "L": 50, "XC": 90, "C": 100, "CD": 400, "D": 500,
                        "CM": 900, "M": 1000}
    if roman_string.isalpha() is False or roman_string is None:
        return 0
    upper_roman_string = roman_string.upper()
    sum = 0
    for k, v in roman_dictionary.items():
        if upper_roman_string == k:
            return v
        for i in range(len(upper_roman_string)):
            if upper_roman_string[i:i + 2] == k:
                sum = sum + v
            else:
                if upper_roman_string[i] == k:
                    sum = sum + v
    return sum
