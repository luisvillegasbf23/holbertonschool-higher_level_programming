#!/usr/bin/python3
''' Write the first class Base '''
import json


class Base:
    ''' class base '''
    __nb_objects = 0

    def __init__(self, id=None):
        ''' constuctor  '''
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        ''' to json  '''
        if list_dictionaries is None:
            return "[]"
        temp = json.dumps(list_dictionaries)
        return temp

    @classmethod
    def save_to_file(cls, list_objs):
        ''' save json in a file  '''
        file = cls.__name__ + ".json"
        temp = []
        if list_objs:
            for i in list_objs:
                temp.append(i.to_dictionary())
        with open(file, "w") as f:
            f.write(Base.to_json_string(temp))
