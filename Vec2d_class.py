# -*- coding: utf-8 -*-
"""
Created on Mon Apr 30 19:52:48 2018

@author: Administrator
"""

from array import array
import math
import sys

class Vector2d(object):
    '''this is the class test'''
    typecode = 'd'   #class_attr
    __slots__ = ('__x','__y')
    
    def __init__(self, x, y):
        self.__x = float(x)
        self.__y = float(y)
        
    @property
    def x(self):
        return self.__x
        
    @property
    def y(self):
        return self.__y
        
    def __iter__(self):
        return (i for i in (self.x, self.y))
    
    def __repr__(self):
        class_name = type(self).__name__
        return '{}:({!r}, {!r})'.format(class_name, *self)
    
    def __str__(self):
        return str(tuple(self))
    
    def test(self):
        print(self) 
    
    def __bytes__(self):
        return(bytes([ord(self.typecode)])+
               bytes(array(self.typecode, self)))
    
    def __eq__(self, other):
        return tuple(self) == tuple(other)
    
    def __hash__(self):
        return hash(self.x) ^ hash(self.y)
    
    def __abs__(self):
        return math.hypot(self.x,self.y)
    
    def __bool__(self):
        return bool(abs(self))
        
    def angle(self):
        return math.atan2(self.y, self.x)
    
    def __format__(self, fmt=''):
        if fmt.endswith('p'):
            fmt = fmt[:-1]
            coords = (abs(self), self.angle())
            outer_fmt = '<{}, {}>'
        else:
            coords = self
            outer_fmt = '({}, {})'
        
        compon = (format(c, fmt) for c in coords)
        return outer_fmt.format(*compon)
    
    @classmethod
    def frombytes(cls, octe):
        typecode = chr(octe[0])
        pass
    
class Test_(object):
    
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def __repr__(self):
        class_name = type(self).__name__
        return '{}:({!r}, {!r})'.format(class_name, *self)
        
    def __iter__(self):
        return (i for i in (self.__x, self.__y))
        
    def test(*self):
        print(self)

    def test2(self):
        print(self)