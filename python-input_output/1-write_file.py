#!/usr/bin/python3
''' Write to a file '''


def write_file(filename="", text=""):
    ''' this function write a file  '''
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(text)
