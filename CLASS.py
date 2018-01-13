# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 22:04:53 2018

@author: Administrator
"""

#practice for Class method and ADT

class rational:
    @staticmethod
    def _gcd(m , n):
        if n == 0:
            m, n = n, m
        while m != 0:
            m, n = n % m, m
        return n
    
    def __init__(self, num, den = 1):
        if not isinstance(num, int) or not isinstance(den, int):
            raise TypeError
        if den == 0:
            raise ZeroDivisionError
        sign = 1
        if num < 0:
            num , sign = -num, -sign
        if den < 0:
            den, sign = -den, -sign
            
        g = rational._gcd(num, den)
        #call function gcd defined static
        
        self._num = sign * (num//g)
        self._den = den//g
        
    #define a method Plus
        
    def plus(self, another):
        _den = self._den * another._den
        _num = (self._num * another._den) + (self._den * another._num)
        
        return rational(_num, _den)
        
    def printf(self):
        print(str(self._num) + "/" + str(self._den))
        
if __name__ == '__main__':  #仅限于这个文件调用此类
    r1 = rational(3, 1)
    r2 = r1.plus(rational(7,15))
    r2.printf()
