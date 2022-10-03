#!/usr/bin/python3
''' Write the first class Base '''


class Base:
    ''' class base '''
    __nb_objects = 0

    def __init__(self, id=None):
        ''' constuctor  '''
        if id == None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
