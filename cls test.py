# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 22:49:04 2018

@author: Administrator
"""

#类定义测试

class countable:
    counter = 0
    
    def __init__(self):    #self只在这个初始化模块作用，而要引用的counter属性是
                            #全局变量，因此需要加全局（外部方法）引用
        countable.counter += 1
    
        #@classmethod类方法的修饰符，表示如下模块中必须约束一个(cls)
    @classmethod       #CLS参数代表此时调用此方法的类，并通过cls访问此类的属性
    def get_count(cls):
        return cls.counter

x1 = countable()
x2 = countable()
x3 = countable()   #计数器的结构类似于循环，将函数调用转化为了类方法的嵌套

print(countable.get_count())

#输出值为3