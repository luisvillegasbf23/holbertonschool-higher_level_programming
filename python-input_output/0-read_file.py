#!/usr/bin/python3
''' Read file '''


def read_file(filename=""):
    ''' this function read a file '''
    with open(filename, 'r', encoding='utf-8') as f:
        for i in f:
            print(i, end='')
