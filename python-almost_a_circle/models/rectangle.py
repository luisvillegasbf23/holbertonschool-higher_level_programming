#!/usr/bin/python3
''' Write the class Rectangle that inherits from Base  '''
from models.base import Base


class Rectangle(Base):
    ''' class  '''
    def __init__(self, width, height, x=0, y=0, id=None):
        ''' constructor  '''
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

        ''' porperties  '''
        @property
        def width(self):
            return self.__width

        @property
        def height(self):
            return self.__height

        @property
        def x(self):
            return self.__x

        @property
        def y(self):
            return self.__y

        ''' setters  '''
        @width.setter
        def width(self, value):
            self.width = value

        @height.setter
        def height(self, value):
            self.height = value

        @x.setter
        def x(self, value):
            self.x = value

        @y.setter
        def y(self, value):
            self.y = value
