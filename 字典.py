# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 20:35:16 2018

@author: Administrator
"""

#test for dictionary

aline_0 = {'x_position': 0, 'y_position' : 25, 'speed' : 'mid', 
'speed2' : 'mid'}
print("original x-p is: " + str(aline_0['x_position']))

#change the position of aline
if aline_0['speed'] == 'slow':
    x_incre = 1
elif aline_0['speed'] == 'mid':
    x_incre = 5
else:
    x_incre = 10

aline_0['x_position'] =+ x_incre
print("new x_postion is: " + str(aline_0['x_position']))

#test for travesal all key-value
for key, value in aline_0.items():
    print("this is the key-value " + str(key)+ " - "+ str(value) +"\n")
    
for value in sorted(aline_0.values()):
    print("this is the value " + str(value) +"\n")
    

#use set to filter the repeat ones
for value in set(aline_0.values()):
    print("this is the key-value " + str(value)) 

#create new game
aline = []

for aline_number in range(30):
    new = {'color': 'green', 'points': '5', 'speed': 'mid'}
    aline.append(new)

for alines in aline[:5]:
    print(alines)
    
#inside dict with list
favor = {
'he': ['python','ruby',3],
'she': ['c', 'jesse', 5],}

for name, p in favor.items():
    print("\n" + str(name).title() + "language is")
    for lang in p:
        print("\t" + str(lang).title())
#with inside dicts

users - {
'key': {'cc',5},
'hhh' : {'skit', 5}
}

