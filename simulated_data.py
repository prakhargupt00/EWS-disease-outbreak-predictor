# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 17:53:16 2019

@author: Prakhar
"""


import pandas as pd 
import numpy as np 
import random
import os 

dir_path = os.path.dirname(os.path.realpath(__file__))


index = [i for i in range(11)]
columns = ["YEAR","ANNUAL_TEMP","ANNUAL_RAINFALL","POPULATION_DENSITY","DISEASE_COUNT"]

#data is in df 
df = pd.DataFrame(index=index , columns=columns)

df.iloc[:,0] = [2000+i  for i in range(11)]


#seed values 
#temperature in degree celcius
df.iloc[0,1]=20.5
 
#rainfall in mm
df.iloc[0,2]= 780

#population density is sq per km 
df.iloc[0,3]= 410

#simulation of temp,rainfall ,disease,population density 
df.iloc[1:,1]= [df.iloc[0,1]+random.uniform(-3.5,3.5) for i in range(10)]


# for city 1 contribution  temp=30 ,rainfall =40 and pop_density=30 starting row contain initial values 
# this is for city 2 
for i in range(5):
    df.iloc[i+1,2] = df.iloc[i,2]+random.uniform(10,50)
for i in range(5):
    df.iloc[i+6,2] = df.iloc[i+5,2] - random.uniform(10,50)


for i in range(10):
    df.iloc[i+1,3] = df.iloc[i,3]+random.randint(1,5)
    

#factor contribution 
contribution = np.array([np.arange(11)]*3) 
contribution = contribution.reshape(11,3)

#initialisation of contribution 
contribution[0,0] = 50 
contribution[0,1] = 20 
contribution[0,2] = 30

for i in  range(10):
    contribution[i+1,0]= 50 + random.uniform(-3.5,3.5)
    contribution[i+1,1]= 20 + random.uniform(-3.5,3.5)
    contribution[i+1,2] = 100 - contribution[i+1,0] -contribution[i+1,1]
    
#normalisation 
temp        = (df.iloc[:,1] - df["ANNUAL_TEMP"].mean())/(df["ANNUAL_TEMP"].std())
rainfall    = (df.iloc[:,2] - df["ANNUAL_RAINFALL"].mean())/(df["ANNUAL_RAINFALL"].std())
pop_density = (df.iloc[:,3] - df["POPULATION_DENSITY"].mean())/(df["POPULATION_DENSITY"].std())

for i in range(11):
    df.iloc[i,4] =(contribution[i][0]/100)*temp[i] +(contribution[i][1]/100)*rainfall[i] +(contribution[i][2]/100)*pop_density[i]
    df.iloc[i,4] = 150 + int(100*df.iloc[i,4])


name = dir_path+ "\\Simulated_datasets\\" +"city2.csv"
df.to_csv(name,index=False)



    
    