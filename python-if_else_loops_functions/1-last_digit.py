#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = number %10
if last_digit > 5:
    print(f"Last digit of {number} is {last_digit} and is greater than 5 and not 0")
elif last_digit == 6:
    print(f"Last digit of {number} is {last_digit} is 0")
else:
    print(f"Last digit of {number} is {last_digit}  is and is greater than 5 and not 0")
