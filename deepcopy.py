# -*- coding: utf-8 -*-
"""
Created on Fri Mar 09 15:01:11 2018

@author: Administrator
"""

import copy

lists = [1, 2, [3, 4]]

shallow = copy.copy(lists)
deep = copy.deepcopy(lists)

cp = lists[:]

