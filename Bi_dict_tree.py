# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 14:04:52 2018

@author: Administrator
"""

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
class BNode:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right
    
    def count_N(self):
        if self is None:
            return 0
        else:
            return 1 + count_N(self.left) + count_N(self.right)

    def pre_nonrec(self):
        s = SStack()
        while self is not None or not s.is_empty():
            while self is not None:
                yield self.data
                s.push(self.right)
                self = self.left
            self = s.pop()

class Dict_Tree:
    def __init__(self):
        self._root = None
    
    def is_empty(self):
        return self._root is None
    
    def search(self, key):
        bt = self._root
        while bt is not None:
            entry = bt.data
            if key < entry.key:
                bt = bt.left
            elif key > entry.key:
                bt = bt.right
            else:
                return entry.value
        return None