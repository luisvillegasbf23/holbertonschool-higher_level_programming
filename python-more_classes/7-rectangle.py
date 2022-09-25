#!/usr/bin/python3
'''Write an empty class Rectangle that defines a rectangle'''


class Rectangle:
    ''' init  '''
    number_of_instances = 0

    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            x = (self.__width * 2) + (self.__height * 2)
            return x

    def __str__(self):
        print_rec = ''
        if self.__width == 0 or self.__height == 0:
            return ''
        for i in range(self.__height):
            for j in range(self.__width):
                print_rec += str(self.print_symbol)
            print_rec += '\n'
        temp = print_rec[:-1]
        return temp

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        '''setter width'''
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        '''setter width'''
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value
