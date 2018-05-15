# -*- coding: utf-8 -*-
"""
Created on Tue May 15 13:15:00 2018

@author: Administrator
"""

for i in range(10):
    for j in range(1, i + 1):
        print("{}X{}={}".format(i, j, i * j))
    print('\n')
        
def arma():
    total = 0
    date = 0
    avg = None
    while True:
        term = yield avg
        total += term
        date += 1
        avg = total/date

def gen():
    yield from range(1,11)
