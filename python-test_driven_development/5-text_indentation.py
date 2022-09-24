#!/usr/bin/python3
''' Write a function that prints a text with 2 new lines after each of thes'''


def text_indentation(text):
    ''' text  identation  '''
    if not isinstance(text, str):
        raise TypeError('text must be a string')
    temp = text.replace('. ', '.\n\n').replace('? ', '?\n\n')
    new_text = temp.replace(': ', '\n\n')
    print(new_text, end='')
