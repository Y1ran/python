# -*- coding: utf-8 -*-
"""
Created on Sun Feb 04 21:44:14 2018

@author: Administrator
"""

#从网页解码数据

from urllib.request import urlopen

fhand = urllib.requests.urlopen("http://www.baidu.com")

for line in fhand.readlines():
    print(line.decode().strip())