# -*- coding: utf-8 -*-
"""
Created on Wed Mar 07 20:09:10 2018

@author: Administrator
"""

import re

x = 'https://raw.githubusercontent.com/wesm/pydata-book/2nd-edition/datasets/babynames/yob1881.txt'
reg = '1[8-9][0-9]{2}'

rex = re.compile(reg)
out = rex.findall(x)
final_out = str(out[0]) +'.txt'
final_year = str(out[0])

y = 'https://raw.githubusercontent.com/wesm/pydata-book/2nd-edition/datasets/babynames/yob'

while True:
    if final_year == 2010:
        break
    else:
        final_year = int(final_year)
        final_year += 1
        print y + str(final_year) + '.txt'
#y = 'https://raw.githubusercontent.com/wesm/pydata-book/2nd-edition/datasets/babynames/yob'
#print y + final_out

