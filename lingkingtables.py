# -*- coding: utf-8 -*-  
""" 
Created on Mon Jan 22 20:35:51 2018 
 
@author: Administrator 
"""  
from __future__ import print_function  
#Python的list结构是分离技术实现的动态线性表  
#此处讨论如何用Python实现链表  
  
############类功能的独立实现###########  
#1.定义类节点  
  
class Lnode:  
    def __init__(self, value, next_ = None):  
        self.value = value  
        self.next_ = next_  
  
  
#2. 创建链表  
head = Lnode(None)  
    #不同于C，链表在插入时相当于自动创建一个非空链表和节点  
    #解释器自动分配内存单元  
#为链表放入元素  
head = Lnode(1)  
p = head  
for i in range(2, 11):  
    p.next_ = Lnode(i)  
    p = p.next_  
#打印链表元素  
p = head  
while p is not None:  
    print(p.value)  
    p = p.next_  
  
  
#3. 插入节点  
'''''首端插入O(1)'''  
q1 = Lnode(13)  
q1.next_ = head.next_    #此处的next没有下划线  
head = q1      #将Q变为头结点,相当于head标示指向q  
  
'''''中端插入O(N)'''  
new_p = head  
i = 0  
while new_p.value != 5:  #在第5个节点后插入节点  
    i += 1  
    new_p = new_p.next_  
insert = Lnode(77)  
insert.next_ = new_p.next_  
new_p.next_ = insert  
#打印所有节点  
p = head  
while p is not None:  
    print(p.value)  
    p = p.next_  
print("")  
  
  
#4.删除节点  
'''''删除头结点'''  
head = head.next_  
'''''删除其他节点'''  
while new_p.value != 5:  #删除新插入的节点  
    i += 1  
    new_p = new_p.next_  
new_p.next_ = new_p.next_.next_  
  
#打印所有节点  
p = head  
while p is not None:  
    print(p.value)  
    p = p.next_  
  
#5.求出链表长度  
  
def leng(head):  
    p, n = head, 0  
    while p is not None:   #在函数体内对参数赋值，改变的是原函数副本变量  
                            #变量的值不变  
        n += 1  
        p = p.next_  
    return n  
  
print(leng(head))  
  
################完整定义链表类######################  
  
class LinkListUnderFlow(ValueError):   #自定义一个异常类  
    pass   
  
class Llist:  
    def __init__(self):  
        self._head = None    #初始化一个节点  
      
    def is_empty(self):  
        return self._head is None  #表示空链表  
      
    def prepend(self, value):  
        self._head = Lnode(value, self._head) #从前端插入节点  
          
    def pop(self):  
        if self._head is None:   
            raise LinkListUnderFlow  
        e = self._head.value           #从头结点弹出元素  
        self._head = self._head.next_  
        return e  
      
    def append(self, value):  
        if self._head is None:   
            self._head = Lnode(value) #如果表为空，则将值插入  
            return                  
        p = self._head  
        while p.next_ is not None:  
            p = p.next_       #表末插入，寻找最后一个元素  
        p.next_ = Lnode(value)  
      
    def find(self, pre):  
        p = self._head  
        while p is not None:  
            if pre == p.value:  #从头结点开始寻找  
                return p.value  
            p = p.next_  
              
    def printall(self):  
        p  = self._head  
        while p is not None:  
            print(str(p.value), end='')  #打印全部节点的值  
            if p.next_ is not None:  
                print('' + '')  
            p = p.next_  
        #print('')  
   #迭代器生成  
  
    def elements(self):  
        p = self._head        #迭代器，自动返回非空链表的所有元素  
        while p is not None:  
            yield p.value  
            p = p.next_          
          
#实例化  
Ins1 = Llist()  
for i in range(10):  
    Ins1.prepend(i)       #将0到9依次从表头压入链表（逆序）  
for i in range(11,20):  
    Ins1.append(i)      #将11到19依次从表末插入链表（顺序）  
Ins1.printall()   
  
  
for i in Ins1.elements():   #利用迭代器的for循环使用更简单  
    print(i)  
