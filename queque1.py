# -*- coding: utf-8 -*-
"""
Created on Thu Mar 08 13:47:30 2018

@author: Administrator
"""

#queue list

from collections import deque

class Squeue():
    def __init__(self, init_len = 8):
        self._len = init_len
        self._elem = [0] * init_len
        self._head = 0
        self._num = 0
    def is_empty(self):
        return self._num == 0
    def peek(self):
        if self._num == 0:
            raise 'QueueUnderflow'
        return self._elem[self._head]
    
    def dequeue(self):
        if self._num == 0:
            return
        e = self._elem[self._head]
        self._head = (self._head + 1) % self._len
        self._num -= 1
        return e
    
    def enqueue(self, e):
        if self._num == self._len:
            self._extent()
        self._elem[(self._head + self._num) % self._len] = e
        self._num += 1
    def extend():
        old_len = self._len
        self._len *= 2
        new_elem = [0]*self._len
        
        for i in range(old_len):
            new_elem[i] = self._elem[(self._head + i) % old_len]
        self._elem, self._head = new_elem, 0