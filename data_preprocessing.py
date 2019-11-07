# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 11:18:05 2019

@author: Prakhar
"""

import numpy as np 
import pandas as pd  
import matplotlib.pyplot as pyt
import os 

dir_path = os.path.dirname(os.path.realpath(__file__))

def if_value_missing():
    
    for i in range(len(combine)):
        if i!=0 :
            if combine.iloc[i,1] != combine.iloc[i-1,1]+1 and combine.iloc[i,1]!= 1901:
                print(i)
            if combine.iloc[i,1] == 1901 and combine.iloc[i-1,1] != 2017:
                print(i)

#getting the data from the file 

#IMPORTANT NOTE RAINFALL_MAIN_CSV HAS  DATA OF DENGUE CASES AS WELL
rainfall_filename = "__rainfall_main.csv"
rainfall = pd.read_csv(rainfall_filename)

temp_filename = "temp_India_1901_2016_main.csv"
temp = pd.read_csv(temp_filename)

pop_den_filename = "population_density_main.csv"
pop_den = pd.read_csv(pop_den_filename)


combine = pd.concat([rainfall.iloc[0:,0:2] ,rainfall.iloc[0:,14:]],axis=1)

temp = temp.iloc[0:,13:]
temp = temp.rename(columns={"ANNUAL":"ANNUAL_TEMP"})

repeat = temp 

for i in range(35):
    repeat = repeat.append(temp,ignore_index=True)  


#rainfall and temperature AND DENGUE CASES   4212 rows x 13 columns
combine = pd.concat([combine,repeat],axis=1)

#COMBINE = RAINFALL AND TEMPERATURE AND DENGUE 
#POP_DEN = SEX RATIO AND POPULATION DENSITY STATE WISE IN DIFFERENT REGIONS 

# Putting data of each subdivision in seperate file 

for i in range(0,len(combine),117):
    df_new = combine.iloc[i:i+117,:]
    name = dir_path+ "\\Datasets\\" +  df_new.iloc[0,0]+".csv"
    print(name)
    df_new.to_csv(name,index=False)
    
    


        
