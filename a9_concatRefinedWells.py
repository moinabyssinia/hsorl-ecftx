"""
Created on Wed Aug 25 15:31:00 2021

this program:
*concatenates the individual refinedWells 

@author: Michael Getachew Tadesse

"""

import os
import numpy as np
import pandas as pd

dirHome = "C:\\Users\\mi292519\\Documents\\hazenStuff\\refinedWellMultipleLayers"
dirOut = "C:\\Users\\mi292519\\Documents\\hazenStuff"

os.chdir(dirHome)

wellList = os.listdir()

# create empty dataframe
df = pd.DataFrame(columns = ['Unnamed: 0', 'layer', 'row', 'columns', 'withdrawal', 'name', 'mon',
       'year', 'monYear', 'rowColPermit', 'rowcol', 'county'])

for well in wellList:
    print(well)
    newDf = pd.read_csv(well)
    newDf.columns = columns = ['Unnamed: 0', 'layer', 'row', 'columns', 'withdrawal', 'name', 'mon',
       'year', 'monYear', 'rowColPermit', 'rowcol', 'county']
    df = pd.concat([df, newDf], axis = 0)

df.reset_index(inplace = True)
df.drop(['Unnamed: 0', 'index'], axis = 1, inplace = True)

print(df.columns)

# save concatenated well data
os.chdir(dirOut)
df.to_csv("refinedWellsConcat.csv")


# open "ecftx_tr_20190329_GLRSTA_Counties_removedRepWells" and add it
newDat = pd.read_csv("ecftx_tr_20190329_GLRSTA_Counties_removedRepWells_reversedWithdrawal.csv") 
newDat.reset_index(inplace = True)
newDat.drop(['Unnamed: 0', 'index'], axis = 1, inplace = True)

print(newDat)

# add the refined wells
allWells = pd.concat([newDat, df], axis = 0)

print(allWells)

allWells.to_csv("ecftx_tr_20190329_GLRSTA_Counties_allWells.csv")
