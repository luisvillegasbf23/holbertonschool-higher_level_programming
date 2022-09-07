#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
temp = number % 10
message = 'Last digit of'

if temp > 5:
    print(f'{message} {number} is {temp} and is greater than 5')
if temp == 0:
    print(f'{message} {number} is {temp} and is 0')
if temp < 6 & temp != 0:
    print(f'{message} {number} is {temp} and is less than 6 and not o')
