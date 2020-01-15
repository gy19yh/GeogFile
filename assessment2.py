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

###### allow user to set the number of bateria and check whether is digit or not ###
chance = 3
while True:
    num_of_agents = input('How much bateria You prefer to lease:')
    
    if chance > 1:
        
        if num_of_agents.isdigit():
            break
    
        else:
            print('You must input number! Without any letter and symbol!') 
            print('You still have', chance-1,'chances')
            chance -= 1
            continue
    
    else:
         print('You run out of all opportunities')
         raise SystemExit 
         

temp = int(num_of_agents)  
num_of_iterations = 500 
agents = []
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
        if value != 0:
            x = row.index(value)
            y = items
              
    items += 1
     
matplotlib.pyplot.scatter(x, y, marker='*',color='red')


##### step 2: where bacteria will end up #####
for i in range(temp):
    agents.append(agentframework2.Agent(x,y,z))
      
for i in range(temp):  
    while agents[i].z != 0:
        agents[i].Hori() 
        agents[i].Vert()       
 
##### step 3: Draws a density map of where all the bacteria end up as an image and displays it on the screen ####    
for i in range(temp):   
    environment[agents[i].y][agents[i].x] += 10
    #matplotlib.pyplot.scatter(agents[i].x,agents[i].y,marker='.')
      
matplotlib.pyplot.ylim(0, 300)
matplotlib.pyplot.xlim(0, 300)
matplotlib.pyplot.imshow(environment)
matplotlib.pyplot.show()
print('Weapon located at the STAR point')
print('The altitude of resource is', z,'meters')

##### step 4: write the density map into txt file##########
output=[]
output.append('X'+'Y')
for i in range(temp): 
    location=[]
    location.append(agents[i].y)
    location.append(agents[i].x)
    output.append(location)  
    
f = open('location.txt', 'w', newline='')
writer = csv.writer(f, delimiter=',')
for i in output:
    writer.writerow(i)
f.close()
