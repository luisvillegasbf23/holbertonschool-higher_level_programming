#!/usr/bin/python3
''' Exact same object  '''


def is_same_class(obj, a_class):
    ''' function  '''
    if type(obj) == bool:
        return False
    if type(obj) is None:
        return False
    if type(obj) == list:
        return False
    if isinstance(obj, a_class):
        return True
    else:
        return False
