#!/usr/bin/python3
'''  Class to JSON  '''


def class_to_json(obj):
    ''' function  '''
    new_obj = obj.__dict__
    return new_obj
