#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = (abs(numbre)) % 10
if last > 5:
    print("last of digit of {} is {} and is greater than 5".format(number, last))
if last == 0:
    print("last digit of {} is {} and is 0".format(number, last))
if last < 0 and last != 0:
    print("last digit of {} is {} and is less than 6 and not 0".format(number,-last))
