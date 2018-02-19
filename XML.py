# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 19:39:26 2018

@author: Administrator
"""

#XML parse练习
#XML模式树分解

import xml.etree.ElementTree as ET

Inp = '''
<stuff>
    <users>
        <user x = '2'>
            <name>Chuck</name>
            <id>001</id>
        </user>
        <user x = "7">
            <name>Brent</name>
            <id>009</id>
        </user>
    </users>
</stuff>'''

stuff = ET.fromstring(Inp)
lst = stuff.findall('users/user')
print('User count: ', len(lst))

for item in lst:
    print('Name', item.find('name').text)
    print('ID', item.find('id').text)
    print('attributes', item.get("x"))
        