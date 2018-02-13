# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 21:10:40 2018

@author: Administrator
"""

#调用API与request

import requests
import json
from django.db import models
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'

r = requests.get(url)
print("status:", r.status_code)

response = r.json()
print(response.keys())
print("total: ", response['total_count'])
repo = response['items']
print("return: ", len(repo))

repo1 = repo[0]
#print(repo)

for key in sorted(repo1.keys()):
    print(key)