# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 19:51:59 2019

@author: Administrator
"""
import csv
import matplotlib
import agentframework2
import matplotlib.pyplot 



###### Set the variables ########
num_of_agents = 5000
num_of_iterations = 500 
agents = []
z = 75

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
            
matplotlib.pyplot.scatter(x, y, marker='*')

##### step 2: where bacteria will end up #####
for i in range(num_of_agents):
    agents.append(agentframework2.Agent(x,y,z))
      
for i in range(num_of_agents):  
    while agents[i].z != 0:
        agents[i].Hori() 
        agents[i].Vert()       
 
##### step 3: Draws a density map of where all the bacteria end up as an image and displays it on the screen ####    
for i in range(num_of_agents):   
    matplotlib.pyplot.scatter(agents[i].x,agents[i].y,marker='.')
      
matplotlib.pyplot.ylim(0, 300)
matplotlib.pyplot.xlim(0, 300)
matplotlib.pyplot.imshow(environment)
matplotlib.pyplot.show()
print('Weapon located at the STAR point')


##### step 4: write the density map into txt file##########
output=[]
output.append('X'+'Y')
for i in range(num_of_agents): 
    location=[]
    location.append(agents[i].x)
    location.append(agents[i].y)
    output.append(location)  
    
f = open('location.txt', 'w', newline='')
writer = csv.writer(f, delimiter=',')
for i in output:
    writer.writerow(i)
f.close()
