"""
Created on Sat Aug 21 16:31:00 2021
this program separates dataframe columns
into delimited version

adds the stress period for each row

@author: Michael Tadesse
"""


import os 
import numpy as np
import pandas as pd


def separateColumn(dat):
    """  
    this function separates the concatenated columns into 
    several columns
    """
    dat = pd.read_csv("outfile.csv")

    separatedDat = dat['0'].str.split(expand = True)

    separatedDat.to_csv("ecftx_tr.20190329.csv")

    return separatedDat

dat = pd.read_csv("ecftx_tr.20190329.csv")
# dat.drop('Unnamed: 0', axis = 1, inplace=True)
dat.columns = ['index','layer', 'row', 'columns', 'withdrawal', \
        'name', 'mon', 'year']

print(dat)

monUnique = (dat['mon']).unique()
yrUnique = (dat['year']).unique()

print(monUnique)
print(yrUnique)

#########################################
# # find the change in stress period
# print(dat[dat['layer'] == 116883])
changeYears = dat[dat['layer'] == 116883]
print(changeYears)
# changeYears.to_csv("stressYears.csv")
#########################################

for inx in range(len(changeYears)):
    print(inx)
    if inx == len(changeYears)-1:
        print("final row") 
        # print(changeYears['year'][inx])
        dat.loc[(dat['index'] >= changeYears.iloc[inx, 0]), 'year'] = \
                changeYears.iloc[inx, 7]
        
        print(changeYears.iloc[inx, 7])

        dat.loc[(dat['index'] >= changeYears.iloc[inx, 0]), 'mon'] = \
                changeYears.iloc[inx, 6]
    else:
        dat.loc[(dat['index'] >= changeYears.iloc[inx, 0]) & \
                (dat['index'] < changeYears.iloc[inx+1, 0]), 'year'] = \
                        changeYears.iloc[inx, 7]
        
        print(changeYears.iloc[inx, 7])
        
        dat.loc[(dat['index'] >= changeYears.iloc[inx, 0]) & \
                (dat['index'] < changeYears.iloc[inx+1, 0]), 'mon'] = \
                        changeYears.iloc[inx, 6]

print(dat)

# dropping redundant rows with stress periods
print(dat[dat['layer'] == 116883])

dropIndices = dat[dat['layer'] == 116883].index
print(dropIndices)

dat = dat.drop(index = dropIndices)

print(dat[dat['layer'] == 116883])

print(dat)

# fill in the first year with -AVE 2003
dat.loc[(~dat['year'].notnull()), 'year'] = 2003
dat.loc[(~dat['mon'].notnull()), 'mon'] = "AVE"



# save dat
dat.to_csv("ecftx_tr_20190329_stressPeriod_v2.csv")