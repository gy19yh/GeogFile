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
    # Bacteria move horizontally by the influence of wind
    # defined east in the x coorderate and north in the y coorderate as positive
    def Hori(self) :
        rate = random.random()
        if rate <= 0.05:          # there is 5% chance
            self.x = (self.x - 1) # the bateria will blow to west 1 meter
        elif 0.05 < rate <= 0.15: # there is 10% chance
            self.y = (self.y - 1) # the bateria will blow to south 1 meter
        elif 0.15 < rate <= 0.25: # there is 10% chance
            self.y = (self.y + 1) # the bateria will blow to north 1 meter
        else:                     # there is 75% chance  
            self.x = (self.x + 1) # the bateria will blow to east 1 meter
    
    # Bateria move vertial
    # defined up as positive way and down as the negative way
    def Vert(self):
        if self.z > 75:                 # check whether the weapon above 75 meters high
            rate = random.random()
            if rate <= 0.20:            # there is 20% chance
                self.z += 1             # the bateria will rise 1 meter by turbulance
            elif 0.20 < rate <= 0.30:   # there is 10% chance
                self.z = self.z         # the bateria will stay at same level
            else:                       # there is 70% chance
                self.z -= 1             # the bateria will drop 1 meter
        else:
            self.z -= 1                 # if the height of weapon below 75 meters it will not influence by turbulance
                                        # the bateria will drop 1 meter a second