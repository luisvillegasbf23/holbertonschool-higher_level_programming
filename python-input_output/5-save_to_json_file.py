#!/usr/bin/python3
'''   Save Object to a file '''


import json


def save_to_json_file(my_obj, filename):
    ''' function '''
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(json.dumps(my_obj))
