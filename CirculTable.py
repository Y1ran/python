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
#头结点由_tail._next隐式说明，不单独构造

class Clist:
    def __init__(self):
        self._tail = None  #定义一个尾结点
        
    def is_empty(self):
        return self._tail is None
        
    def prepend(self, value):  #前端插入
        p = Lnode(value)
        if self._tail is None:
            p._next = p    #利用链表指针p判断空链表
            self._tail = p   #如果为空则插入并令P为尾结点
        else:
            p._next = self._tail._next
            self._tail._next = p
    
    def append(self, value):  #
        self.prepend(value)
        self._tail = self._tail._next
    #直接在尾部之后插入并将尾节点后移一位,相当于在后端插入
    def pop(self):  
        if self._tail is None:
            raise LinkListUnderFlow("in pop of Clist")
        p = self._tail._next
        if self._tail is p:         #只有一个节点时弹出后表为空
            self._tail = None
        else:
            self._tail._next = p.value
        return p.value
        
    def printall(self):   #打印所有链表元素
        if self.is_empty():
            return
        p = self._tail._next  #通过指针p从头结点开始
        while p:
            print(p.value, end="")
            if p is self._tail:
                break
            p = p._next
    
#Ins实例化测试
    
Ins2 = Clist()
Ins2.prepend(99)

print("  test is commit...  ")

for i in range(1,21):
    Ins2.append(int(i))

Ins2.printall()

            