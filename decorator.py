# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 20:44:04 2018

@author: Administrator
"""

def deck(func):
    def in_deck(x, y):
        print("in it")
        func(x * 2, y * 2)
    
    print("call deck")
    return in_deck
    
@deck
def mus(x, y):
    print x + y
    

mus(1, 12)

def iter_test(n):
    
    i = 0
    while i != n:
        yield i
        i += 1
    print("this is end")
    
    #eturn 0

for i in iter_test(10):
    print i