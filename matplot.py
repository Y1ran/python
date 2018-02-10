# -*- coding: utf-8 -*-
"""
Created on Fri Feb 09 14:35:47 2018

@author: Administrator
"""

import matplotlib.pyplot as mp
'''
squar = [ x * x for x in range(1, 1001)]
x_inp = [x for x in range(1, 1001)]
mp.plot(squar)
mp.show()

mp.plot(x_inp, squar, linewidth=5)
mp.title("Square Number", fontsize = 24)
mp.xlabel("Value", fontsize = 14)
mp.ylabel('Square of value', fontsize = 14)

mp.scatter(x_inp, squar, c= squar, edgecolor = 'none', cmap = mp.cm.Blues)
mp.savefig('suqare.png', bbox_inches = 'tight')'''

"""随机漫步"""

from random import choice

class RandomWalk():
    
    def __init__(self, num_points = 5000):
        self.num_points = num_points
        
        self.x_values = [0]
        self.y_values = [0]
        
    def fill_walk(self):
        while len(self.x_values) < self.num_points:
            x_dir = choice([1, -1])
            x_dis = choice([0, 1, 2, 3, 4])
            x_step = x_dir * x_dis
            
            y_dir = choice([1, -1])
            y_dis = choice([0, 1, 2, 3, 4])
            y_step = y_dir * y_dis
            
            if x_step == 0 and y_step == 0:
                continue
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step
            
            self.x_values.append(next_x)
            self.y_values.append(next_y)

#测试随机漫步类

RW = RandomWalk()
RW.fill_walk()

mp.axes().get_xaxis().set_visible(False)

mp.scatter(RW.x_values, RW.y_values, s =5)
mp.show()