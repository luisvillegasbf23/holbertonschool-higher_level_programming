#!/usr/bin/python3
''' Write the class Square that inherits from Rectangle: '''
from .rectangle import Rectangle


class Square(Rectangle):
    ''' class rentangle '''
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """prints the rectangle with his different attributes"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"


