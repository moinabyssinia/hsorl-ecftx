"""
Created on Wed Aug 25 07:30:00 2021

this program:
*separates the wells that cut through multiple layers 

@author: Michael Getachew Tadesse

"""
import os 
import pandas as pd

dirHome = "C:\\Users\\mi292519\\Documents\\hazenStuff"
dirOut = "C:\\Users\\mi292519\\Documents\\hazenStuff\\wellMultipleLayers"

# read raw data
dat = pd.read_csv("ecftx_tr_20190329_GLRSTA_Counties.csv")
dat.reset_index(inplace = True)
dat.drop(['Unnamed: 0', 'Unnamed: 0.1', 'index', 'level_0'], axis = 1, inplace = True)

layers = dat['layer'].unique()
monYear = dat['monYear'].unique()

# loop through each monYear
for my in monYear:
    os.chdir(dirHome)
    print(my)
    currentDat = dat[dat['monYear'] == my]

    repWells = currentDat[currentDat['rowColPermit'].duplicated(keep = False)]
    # print(repWells)

    # drop repWells from original dataframe
    dat.drop(repWells.index, axis = 0, inplace = True)


    # save as csv
    os.chdir(dirOut)
    repWells.to_csv(my.split('.')[0] + ".csv")

# save truncated dat
os.chdir(dirHome)
dat.to_csv("ecftx_tr_20190329_GLRSTA_Counties_removedRepWells.csv")
