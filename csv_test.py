# -*- coding: utf-8 -*-
"""
Created on Fri Feb 09 16:12:00 2018

@author: Administrator
"""

import csv
from matplotlib import pyplot as plt
from datetime import datetime
filename = 'sitka_weather_07-2014.csv'
with open(filename) as fh:
    reader = csv.reader(fh)
    header = next(reader)
#使用enumera获取指标和值    
    for index, col in enumerate(header):
        print(index, col)

#获得最高气温
filename = 'sitka_weather_2014.csv'
with open(filename) as fh:
    reader = csv.reader(fh)
    header = next(reader)
    high, low, date = [],[],[]
    
    for row in reader:
        high.append(int(row[1]))
        current = datetime.strptime(row[0], '%Y-%m-%d')
        date.append(current)
        low.append(int(row[3]))
        
print(high)

fig = plt.figure(dpi = 123, figsize = (10, 6))
plt.plot(date, high, c = 'red', alpha=0.5)
plt.plot(date, low, c = 'blue', alpha=0.5)

plt.fill_between(date, high, low, facecolor='pink', alpha = 0.1)

plt.title("Square Number", fontsize = 24)
plt.xlabel("Value", fontsize = 14)
fig.autofmt_xdate()
plt.ylabel('Square of value', fontsize = 14)
plt.show()

'''世界人口地图'''

import json

filename_ = 'population_data.json'
with open(filename_) as fhand:
    pop_data = json.load(fhand)
    
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country = pop_dict['Country Name']
        population = pop_dict['Value']
        print(country + ":" + population)