#!/usr/bin/python3
'''  Create object from a JSON file  '''


import json


def load_from_json_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        json_str = f.read()
        obj = json.loads(json_str)
        return obj
