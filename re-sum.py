# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 22:07:27 2018

@author: Administrator
"""

#The basic outline of this problem is to read the file, look for 
#integers using the re.findall(), 
#looking for a regular expression of '[0-9]+' 
#and then converting the extracted strings to integers 
#and summing up the integers.

import re
import math

fh = open('regex.txt','r')
out_put = []    #this list is for line operation
result = []      #this is for sum operation

for line in fh.readlines():
    line = line.strip()
    if not len(line):
        continue           #jump the blank lines
    out_put = re.findall('[0-9]+',line)

    for item in range(0, len(out_put)):
        if out_put:
            """
            #del out_put    I tried to delete the empty element in list
            #print(out_put)     but actually it wasn't needed
            """
            for k in out_put:
                result.append(int(k))   #give integer into result list
        
#print(type(out_put))   check the output test
print(type(result))

print(result)
#for out in out_put:
   # print(out)
    
#total sum inside list:
Sum_result = 0

for k in result:
    Sum_result = Sum_result + k

print("The total sum of text is " + str(Sum_result) + ".")
  

fh.close()

    
