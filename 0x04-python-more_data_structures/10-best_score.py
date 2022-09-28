#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        for k, v in a_dictionary.items():
            if v == (sorted(a_dictionary.values()))[-1]:
                return k
