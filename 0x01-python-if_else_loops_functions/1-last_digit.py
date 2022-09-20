#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    last_digit = (-1 * number) % 10
else:
    last_digit = number % 10
print(f"Last didigit of {number} is", end=" ")
if last_digit > 5:
    print(f"{last_digit} and is greater than 5")
elif last_digit == 0:
    print(f"{last_digit} and is zero")
elif last_digit < 6 and last_digit != 0:
    print(f"{last_digit} and is less than 6 and not 0")
