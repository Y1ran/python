# -*- coding: utf-8 -*-
"""
Created on Wed Mar 07 19:35:58 2018

@author: Administrator
"""

import pandas as pd

unames = ['user_id', 'gender', 'age', 'occupation','zip']
users = pd.read_table('users.dat', sep='::',
                      header=None, names=unames)
        
rnames = ['user_id', 'movie_id', 'rating', 'timestamp'] 
ratings = pd.read_table('ratings.dat', sep='::', 
                        header= None, names= rnames)
mnames = ['movie_id', 'title', 'genres'] 
movies = pd.read_table('movies.dat', 
                         sep='::', header= None, names= mnames)

#Wes McKinney. 利用Python进行数据分析 (O'Reilly精品图书系列) (Kindle Locations 607-608). 机械工业出版社. Kindle Edition. 
data = pd.merge(pd.merge(ratings, users), movies)

#print (data.ix[0])

#mean_rate = data.pivot_table('rating', rows= 'title',
                           #  cols = 'gender', aggfunc ='mean')
rating_by = data.groupby('title').size()
print(rating_by[:10])
                            
active = rating_by.index[rating_by >= 250]
print (active)


print(users[:5])
