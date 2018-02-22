# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 22:26:24 2018

@author: Administrator
"""


import urllib
import xml.etree.ElementTree as ET


'http://py4e-data.dr-chuck.net/comments_9856.xml'
while True:
    address = input('Enter location: ')
    if len(address) < 1: break

 
    uh = urllib.urlopen(address)
    data = uh.read()
    print('Retrieved', len(data), 'characters')
    
    results = data.decode()
    
    tree = ET.fromstring(results)

    #result = tree.find('count').text

    lst = []
    
    lst = tree.findall('.//comment')
    
    result = []
    for i in lst:
       temp = i.find('count').text
       result.append(int(temp))
    
    print sum(result)
    
    #print(lst)
    #print(sresults)
    #print(type(results))
    #This took me hrs to completed
