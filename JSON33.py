# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 22:44:40 2018

@author: Administrator
"""

#JSON作业，WEB抓取

import json
import urllib
import sys


serviceurl = 'http://py4e-data.dr-chuck.net/comments_9857.json'


address = input('Enter location: ')
try:
    if len(str(address))  < 1: 
        print("please enter the command\n")
        exit()
except:
    pass

finally:
    
    url = serviceurl
    print('Retrieving...', url)
    
    uh = urllib.urlopen(url)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')
    print(data)

    
    info = json.loads(data)
    print(info)
    
    lst = info.values()
    lst = lst[1]
    
    print lst
    
    items = []
    for item in lst:
        x = item.values()
        items.append(x[0])
    
    print sum(items)
        
       
    
#    fp = file('test22.txt', 'w')
#
#    
#    json.dump(data, fp)
#    
#   3 fh = fp.read()
#   # info = json.load(fp)
#    print(fh)
    
#print(info)
# print('User count:', len(info))

