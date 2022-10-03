#!/usr/bin/python3
''' Write the class Rectangle that inherits from Base  '''
from models.base import Base


class Rectangle(Base):
    ''' class  '''
    def __init__(self, width, height, x=0, y=0, id=None):
        ''' constructor  '''
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

        ''' width  '''
        @property
        def width(self):
            return self.__width

        @width.setter
        def width(self, value):
            self.__width = value

        ''' height '''
        @property
        def height(self):
            return self.__height

        @height.setter
        def height(self, value):
            self.__height = value

        ''' x '''
        @property
        def x(self):
            return self.__x

        @x.setter
        def x(self, value):
            self.__x = value

        ''' y '''
        @property
        def y(self):
            return self.__y
        @y.setter
        def y(self, value):
            self.__y = value
