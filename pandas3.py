# -*- coding: utf-8 -*-
"""
Created on Wed Mar 07 20:45:02 2018

@author: Administrator
"""

import pandas as pd
import numpy as np

names1881 = pd.read_csv('yob/yob1881.txt', names=['name', 'sex',
                                                 'births'])
#print (names1881)

#print names1881.groupby('sex').births.sum()

years = range(1881, 2011)

pieces = []
cols = ['name', 'sex','births']

for y in years:
    path = 'yob/yob%d.txt' % y
    frame = pd.read_csv(path, names = cols)
    frame['year'] = y
    
    pieces.append(frame)

names = pd.concat(pieces, ignore_index = True)

total_bir = names.pivot_table(index='year'
                , columns='sex',aggfunc=sum)


def add_prop(group):
    births = group.births.astype(float)
    group['prop'] = births / births.sum()
    return group

names = names.groupby(['year','sex']).apply(add_prop)

def get_top1000(group):
    return group.sort_index(by='births', ascending=False)[:1000]

grouped = names.groupby(['year','sex'])
top1000 = grouped.apply(get_top1000)

boys = top1000[top1000.sex == 'M']
girls = top1000[top1000.sex == 'F']


total = top1000.pivot_table('prop', index='year',
                            columns='sex',aggfunc=sum)

print total.plot(title='sum of 1000', yticks=np.linspace(0, 1.2, 13),
                 xticks = range(1880,2020,10))

