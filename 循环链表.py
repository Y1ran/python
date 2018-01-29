# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 21:14:29 2018

@author: Administrator
"""
from __future__ import print_function
from lingkingtables import Lnode
from lingkingtables import Llist
from lingkingtables import LinkListUnderFlow
#Python数据结构之循环单链表
#增加了尾结点，使得尾部查询更优化，且便于循环的实现
class Clist:
    def __init__(self):
        self._tail = None  #定义一个尾结点
        
    def is_empty(self):
        return self._tail is None
        
    def prepend(self, value):  #前段插入
        p = Lnode(value)
        if self._tail is None:
            p._next = p    #
            self._tail = p
        else:
            p._next = self._tail.next
            self._tail._next = p
    
    def append(self, value):  #
        self.prepend(value)
        self._tail = self._tail._next
    
    def pop(self):  
        if self._tail is None:
            raise LinkListUnderFlow("in pop of Clist")
        p = self._tail._next
        if self._tail is p:         #zhiyou yige jiedian
            self._tail = None
        else:
            self._tail._next = p.value
        return p.value
        
    def printall(self):   #
        if self.is_empty():
            return
        p = self._tail._next  #congtou kaishi
        while p:
            print(p.value)
            if p is self._tail:
                break
            p = p._next
    
#Ins
    
Ins2 = Clist()
Ins2.prepend(99)
for i in range(0,21):
    Ins2.append(int(i))

Ins2.printall()

            