# -*- coding: utf-8 -*-
"""
Created on Sun Apr 01 21:40:15 2018

@author: Administrator
"""

class Person(object):

    __slots__ = ('name', 'gender')

    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

class Student(Person):

    __slots__ = ('name', 'gender', '__score')

    def __init__(self, name, gender, score):
        self.name = name
        self.gender = gender
        self.__score = score
        
    @property
    def score(self):
        return self.__score
    @score.setter
    def score(self, score):
        self.__score = score
        
    def __str__(self):
        return '%d' % self.__score
        
    #__repr__ == __str__


s = Student('Bob', 'male', 59)
s.name = 'Tim'
s.score = 99
print s.score