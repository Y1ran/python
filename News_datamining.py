# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 20:53:08 2018

@author: Administrator
"""

import jieba
import jieba.posseg as pseg
import matplotlib.pyplot as plt
import numpy as np
from os import path
import pandas as pd
import re
import requests
from scipy.misc import imread
import time
from wordcloud import WordCloud
from future_builtins import *

def fetch_sina_news():
    Pattern = re.compile('.shtml" target="_blank">(.*?)</a><span>(.*?)</span></li>')
    Base_url = "http://roll.news.sina.com.cn/news/gnxw/gdxw1/index_"
    Max_page = 2
    
    with open('subjects.txt','w') as f:
        for i in range(1, Max_page):
            print('Downloading page #{}'.format(i))
            r = requests.get(Base_url + str(i) + '.shtml')
            r.encoding = 'gb2312'
            data = r.text
            p = re.findall(Pattern, data)
            
            for s in p:
                f.write(s[0].encode('utf-8'))
            time.sleep(5)

def extract_words():
    with open ('subjects.txt','r') as f:
        new_subjects = f.readlines()
    
    new_set = set()
    for line in open('stopwords.txt'):
        line = line.encode('utf-8')
        try:
            new_set.add(line)
        except:
            continue
    stop_words = new_set
    newslist = []
    
    for subject in new_subjects:
        if subject.isspace():
            continue
    
        word_list = pseg.cut(subject)
        for word, flag in word_list:
            if not word in stop_words and flag == 'n':
                newslist.append(word)
    
    d = path.dirname(__file__)
    mask_image = plt.imread(d + "/micket.png")
    
    font = 'simhei.ttf'
    content = ''.join(newslist)
    wordcloud = WordCloud(font_path=font, background_color='white',
                          max_words=40).generate(content)

    plt.imshow(wordcloud)
    plt.axis("off")

    plt.show()
    wordcloud.to_file('wordcloud.jpg')


if __name__ == "__main__":
    fetch_sina_news()
    extract_words()