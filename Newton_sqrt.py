# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 18:45:26 2018

@author: Administrator
"""

def format_name(s):
    if len(s) == 0:
        return 0
    if not str(s).istitle():
        return s.title()

print map(format_name, ['adam', 'LISA', 'barT'])
import math

print 'sdDsd'.istitle()

def sqrt_newton(num):  
    x = math.sqrt(num)  
    y = num / 2.0  
    while abs(y - x) > 0.001:  
        y = (y + num / y)/2  
    bound = y - int(y)
    if bound == 0:
        return int(y)
    else:
        return y

def dec(func):
    print 1
    def in_dec(num):
        y = func(num)
        bound = float(y) - int(y)
        if bound < 0.00000001:
            return int(y)
        else:
            return y

    return in_dec

@dec
def my_sqrt(num):
    print 4
    return math.sqrt(num)
    

print my_sqrt(5)

def prod(lst):
    while lst:
        for i in lst[1:]:
            yield i
    return


def prod2(lst):
    prod = 1
    for i in lst:
        prod = i * prod
    return prod
lst = [2,4,3,1,2]

test = prod2(lst)
print test