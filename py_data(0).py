# -*- coding: utf-8 -*-
"""
Created on Tue Mar 06 22:21:36 2018

@author: Administrator
"""
import json
from collections import Counter
from pandas import DataFrame, Series
import pandas as pd; import numpy as np
#import matplotlib as plt


path = 'usagov_bitly_data2013-05-17-1368832207.txt'
with open(path) as fh:
    lines = fh.readline()

print (lines)

record = [json.loads(line) for line in open(path)]
#print record[0]

frame = DataFrame(record)
#print frame


clean_tz = frame['tz'].fillna('Missing')
clean_tz[clean_tz == ''] = 'Unknown'
tz_count = clean_tz.value_counts()

print tz_count[:10].plot(kind='barh', rot=0)

time_z = [tz['tz'] for tz in record if 'tz' in tz]
#print time_z

def get_count(seq):
    counts = {}
    for x in seq:
        counts[x] = counts.get(x, 0) + 1
    return counts

#counts = get_count(time_z)
counts = Counter(time_z)

#print counts['America/Los_Angeles']
print counts.most_common(10)

cframe = frame[frame.a.notnull()]

ops = np.where(cframe['a'].str.contains('Windows'), 'Windows','Not Windows')
print ops[:5]