# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 20:04:50 2018

@author: Administrator
"""

from functools import reduce
from operator import sub,mul,itemgetter, methodcaller

class fact(object):
    '''factorial func'''
    def __init__(self, number, count=0):
        self.n = number
    
    def factorial(self) :
        return reduce(mul, range(1, n + 1))

    def __call__(self):
        print factorial(self.n)
        

if __name__ == "__main__":
    
    newins = fact(5)
    
    print fact.__doc__
    print type(newins)
    
    newins()
    
    lst = [x for x in range(11)]
    cc = itemgetter(3)
   
    x = methodcaller('upper')
    print x('abc')
    