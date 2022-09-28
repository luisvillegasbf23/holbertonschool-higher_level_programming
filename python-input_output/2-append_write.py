#!/usr/bin/python3
''' Append to a file  '''


def append_write(filename="", text=""):
    ''' append to file '''
    with open(filename, 'a', encoding='utf-8') as f:
        lent_file = f.write(text)
        return lent_file
