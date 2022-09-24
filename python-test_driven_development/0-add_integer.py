#!/usr/bin/python3
''' Write a function that adds 2 integers  '''


def add_integer(a, b=98):
    if type(a) not in [int, float]:
        raise TypeError('a must be an integer')
    if type(b) not in [int, float]:
        raise TypeError('b must be an integer')
    if type(a) == float or type(b) == float:
        a = int(a)
        b = int(b)
    return a + b
