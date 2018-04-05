# -*- coding: utf-8 -*-
"""
Created on Thu Apr 05 21:47:38 2018

@author: Administrator
"""

import requests
from bs4 import BeautifulSoup
import re

sum = 0
r = requests.get('https://book.douban.com/subject/1084336/')
soup = BeautifulSoup(r.text, 'lxml')
pattern = soup.find_all('p','comment-content')
for item in pattern:
    print(item.string)
    
patterns = re.compile('span class="user-stars allstar(.*?)rating"')
p = re.findall(patterns, r.text)

for star in p:
    sum += int(star)
    print star
print(sum)