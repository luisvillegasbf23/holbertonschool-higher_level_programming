#!/usr/bin/python3
'''  Rectangle  '''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """define class Rectangle"""

    def __init__(self, width, height):
        """initialize class base"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
