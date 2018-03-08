# -*- coding: utf-8 -*-
"""
Created on Wed Mar 07 16:07:19 2018

@author: Administrator
"""

#tail_recurs optmize
class StackUnderflow(ValueError):
    pass

class SStack():        #use list as stack class obj
    def __init__(self):
        self._elems = []
    
    def is_empty(self):
        return self._elems == []
    
    def top(self):
        if self._elems == []:
            raise StackUnderflow("in SStack.top()")
        return self._elems[-1]
    def push(self, elem):
        self._elems.append(elem)
    
    def pop(self):
        if self._elems == []:
            raise StackUnderflow("in SStack.top()")
        return self._elems.pop()

#test

def fact(n, sum = 1):
    if n == 0:
        return sum
    else:
        return fact(n - 1, sum * n)

print fact(6)

#type: non-recurs

def nonrec_fact(n):
    res = 1
    stk = SStack()
    
    while n > 0:
        stk.push (n)
        n -= 1
    while not stk.is_empty():
        res *= stk.pop()
    
    return res

print nonrec_fact(5)