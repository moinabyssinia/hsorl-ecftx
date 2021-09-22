"""
Created on Wed Aug 25 08:12:00 2021

this program:
*organizes the multiple wells in such a way that
 the withdrawal is summed up and sign reveresed and 
 layers cut through are marked 

@author: Michael Getachew Tadesse

"""

import os
import numpy as np
import pandas as pd

dirHome = "C:\\Users\\mi292519\\Documents\\hazenStuff\\wellMultipleLayers"
dirOut = "C:\\Users\\mi292519\\Documents\\hazenStuff\\refinedWellMultipleLayers"

os.chdir(dirHome)
monYear = os.listdir()

for my in monYear:
    os.chdir(dirHome)

    print(my)
    dat = pd.read_csv(my)
    
    dat.drop('Unnamed: 0', axis = 1, inplace = True)

    # get unique rowcolPermit
    rowColPermit = dat['rowColPermit'].unique()

    # create empty dataframe - for trend computation 
    df = pd.DataFrame(columns = ['layer', 'row', 'columns', 'withdrawal', 'name',\
            'mon', 'year', 'monYear', 'rocColPermit', 'rowcol', ' county'])

    # loop through unique rowcols
    for rcp in rowColPermit:
        currentDat = dat[dat['rowColPermit'] == rcp]

        layer = currentDat['layer'].unique()
        layerStr = [str(i) for i in layer]
        layerStrJoin = "_".join(layerStr)

        # sum up withdrawal - reverse sign
        withdrawalSum = -1 * np.sum(currentDat['withdrawal'].tolist())

        newDf = pd.DataFrame([layerStrJoin, currentDat['row'].unique()[0],
            currentDat['columns'].unique()[0], withdrawalSum, 
            currentDat['name'].unique()[0],
                currentDat['mon'].unique()[0], currentDat['year'].unique()[0],
                    currentDat['monYear'].unique()[0], currentDat['rowColPermit'].unique()[0],
                        currentDat['rowcol'].unique()[0], currentDat['county'].unique()[0]]).T
        newDf.columns = ['layer', 'row', 'columns', 'withdrawal', 'name',\
            'mon', 'year', 'monYear', 'rocColPermit', 'rowcol', ' county']
        df = pd.concat([df, newDf], axis = 0)


    # save as csv
    os.chdir(dirOut)
    df.to_csv(my)
    