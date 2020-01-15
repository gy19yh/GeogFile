# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 20:42:59 2019

@author: Administrator
"""

import random   

class Agent():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def Hori(self) :
        rate = random.random()
        if rate <= 0.05:
            self.x = (self.x - 1) 
        elif 0.05 < rate <= 0.15: 
            self.y = (self.y - 1) 
        elif 0.15 < rate <= 0.25:
            self.y = (self.y + 1) 
        else: 
            self.x = (self.x + 1)
       
    def Vert(self):
        if self.z > 75:
            rate = random.random()
            if rate <= 0.20:
                self.z += 1
            elif 0.20 < rate <= 0.30:
                self.z = self.z
            else: 
                self.z -= 1
        else:
            self.z -= 1
