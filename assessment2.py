# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 19:51:59 2019

@author: Administrator
"""

import csv
import random
import matplotlib
import agentframework2
import matplotlib.pyplot 



###### Set the variables ########

#num_of_agents = 5000

# allow user to set the number of bateria and check whether is digit or not 
chance = 3
while True:
    num_of_agents = input('How much bateria You prefer to lease:')
# give user 3 times to input the right format#    
    if chance > 1:
        # check the format of input
        if num_of_agents.isdigit():
            break
        # if the user input the wrong format, give the another chance to input the number
        # However, the user only have 3 times to input the number of bateria
        else:
            print('You must input number! Without any letter and symbol!') 
            print('You still have', chance-1,'chances')
            chance -= 1
            continue
    
    else:
         # if the user run out of all chances and still input the wrong format
         # the programme will be shutting down
         print('You run out of all opportunities')
         raise SystemExit # the code aims to shut down the programme
         

temp = int(num_of_agents)  
num_of_iterations = 500 
agents = []

# the height of the building is 75m
# the bateria is above the top of the building. But we not sure how height it is.
# Hence, I set the random height of the weapon 
z = random.randint(75,150)

#print(z)

######### step 1: Pull in the data file   #########
environment = [] # A list name 'environment'
with open('wind.raster.txt', newline='') as csvfile: # open the data file named wind.raster.txt
    reader = csv.reader(csvfile, delimiter=',') # read the data and seperate the data with comma
    for row in reader: 
        rowlist = []
        for value in row: 
            rowlist.append(int(value)) # add the int data value into rowlist
        environment.append(rowlist) # add the 'rowlist' into 'environmrnt'

### located the bacterial weapon and marked as a star ###

items = 0
for row in environment:
    for value in row:
        if value > 0:
            x = row.index(value)
            y = items
              
    items += 1
# after locating the resource of the weapon, mark it as a red star    
matplotlib.pyplot.scatter(x, y, marker='*',color='red')


##### step 2: where bacteria will end up #####
# link the model with the agentframework2 
for i in range(temp):
    agents.append(agentframework2.Agent(x,y,z))
      
for i in range(temp):  
    while agents[i].z != 0:
        agents[i].Hori() 
        agents[i].Vert()       
 
##### step 3: Draws a density map of where all the bacteria end up as an image and displays it on the screen ####    
# after bateria falling on the environment, the value of the certain area plus 10, which makes it more visable
# this is the core of the code to make the density map
for i in range(temp):   
    environment[agents[i].y][agents[i].x] += 10
    #matplotlib.pyplot.scatter(agents[i].x,agents[i].y,marker='.') 

# draw a map with the 300*300 size      
matplotlib.pyplot.ylim(0, 300)
matplotlib.pyplot.xlim(0, 300)
matplotlib.pyplot.imshow(environment) # shows the environment
matplotlib.pyplot.show()

# to show the location of the weapon
print('Weapon located at the STAR point')
# to show the height of the weapon
print('The altitude of resource is', z,'meters')

##### step 4: write the density map into txt file##########
output=[]
# input the title of each row
output.append('X'+'Y')
# input the value of each pair of coordinate
for i in range(temp): 
    location=[]
    location.append(agents[i].x)
    location.append(agents[i].y)
    output.append(location)  

# create the text file and write the value in 
f = open('location.txt', 'w', newline='')
writer = csv.writer(f, delimiter=',')
for i in output:
    writer.writerow(i)
f.close()

