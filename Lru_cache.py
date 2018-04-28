# -*- coding: utf-8 -*-
"""
Created on Sat Apr 28 20:43:10 2018

@author: Administrator
"""
import functools

@functools.lru_cache()
def fib(n):
    if n < 2: 
        return n
    return fib(n-2) + fib(n-1)
    
if __name__ == '__main__':
    print fib(30)