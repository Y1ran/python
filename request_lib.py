# -*- coding: utf-8 -*-
"""
Created on Sat Apr 07 21:27:20 2018

@author: Administrator
"""

import requests

r = requests.get('https://api.douban.com/v2/book/1003078')

import nltk

nltk.download()

import asyncio
