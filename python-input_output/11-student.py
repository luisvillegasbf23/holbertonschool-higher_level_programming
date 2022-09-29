#!/usr/bin/python3
'''  Student to JSON '''


class Student:
    ''' class  '''
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        ''''''
        if attrs is None:
            return self.__dict__
        else:
            dic = {}
            for x in attrs:
                if x in self.__dict__.keys():
                    dic[x] = self.__dict__[x]
            return dic

    def reload_from_json(self, json):
        ''''''
        for key, value in json.items():
            setattr(self, key, value)
