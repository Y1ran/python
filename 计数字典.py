# -*- coding: utf-8 -*-
"""
Created on Sun Feb 04 22:08:46 2018

@author: Administrator
"""

#利用字典进行计数

import collections

list1 = list(x*x for x in range(0,10))
list2 = [x*x for x in range(0,10)]
print(list1, list2)

counts = {}
for i in list1+list2+[1,4,4,9,25,16]:
    counts[i] = counts.get(i, 0) + 1
print counts