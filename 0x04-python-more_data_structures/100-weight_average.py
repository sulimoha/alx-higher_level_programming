#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    sum = 0
    total_weight = 0
    for tulp in my_list:
        sum = sum + tulp[0]*tulp[1]
        total_weight = total_weight + tulp[1]
    average = sum / total_weight
    return average
