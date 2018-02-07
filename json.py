# -*- coding: utf-8 -*-
"""
Created on Wed Feb 07 20:32:47 2018

@author: Administrator
"""

#测试JSON

import json
import sys

number = [x for x in range(0, 111)]
#生成新的json文件
filename = "numbers.json"
with open(filename, 'w') as fh:
    json.dump(number, fh)

print sys.argv[0]

#打开文件

filename2 = sys.argv[0]
with open(filename2, 'r') as fhand:
    print(fhand.read().strip())  #打印代码自身
    
with open(filename, 'r') as fhand:
    for line in fhand.readlines():    
        print(line.strip()) 

with open(filename, 'r') as fhh:
    numbers = json.load(fhh)
print(numbers)

