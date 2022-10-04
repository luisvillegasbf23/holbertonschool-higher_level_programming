#!/usr/bin/python3
''' Write the class Rectangle that inherits from Base  '''
from models.base import Base


class Rectangle(Base):
    ''' Rectangle class  '''
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

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

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        ''' area of rectangle  '''
        return self.__height * self.__width

    def display(self):
        ''' print a rectangle '''

        for y in range(self.__y):
            print('')
        for i in range(self.__height):
            for x in range(self.__x):
                print(' ', end='')
            for j in range(self.__width):
                print('#', end='')
            print('')

    def __str__(self):
        x = self.__x
        y = self.__y
        h = self.__height
        w = self.__width

        return (f'[Rectangle] ({self.id}) {x}/{y} - {w}/{h}')

    def update(self, *args):
        ''' update  '''
        if args is not None:
            if args[0]:
                self.id = args[0]
            if len(args) > 1:
                self.__width = args[1]
            if len(args) > 2:
                self.__height = args[2]
            if len(args) > 3:
                self.__x = args[3]
            if len(args) > 4:
                self.__y = args[4]
