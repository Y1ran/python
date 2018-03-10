# -*- coding: utf-8 -*-
"""
Created on Sat Mar 10 16:49:23 2018

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
            
from queque1 import Squeue

def lev_order(tree):
    '''BFS'''
    Q = Squeue()
    Q.enqueue(tree)
    
    while not Q.is_empty():
        tree = Q.dequeue()
        if tree is None:
            continue
        Q.enqueue(tree.left)
        Q.enqueue(tree.right)
        print(tree.data)

def print_tree(inp):
    print (inp)

def preorder(tree):
    if tree is None:
        return
    print(tree.data)
    preorder(tree.left)
    preorder(tree.right)
    

       
   