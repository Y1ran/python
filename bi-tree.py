# -*- coding: utf-8 -*-
"""
Created on Fri Mar 09 16:22:45 2018

@author: Administrator
"""

def BiTree(data, left=None, right=None):
    return [data, left, right]

def is_empty(btree):
    return btree is None

def root(btree):
    return btree[0]

def left(btree):
    return btree[1]

def right(btree):
    return btree[2]

def set_root(btree, data):
    btree[0] = data
def set_left(btree, data):
    btree[1] = data
def set_right(btree, data):
    btree[2] = data

t1 = BiTree(2, BiTree(4),  BiTree(8))