"""
Created on Wed Aug 25 15:53:00 2021

this program:
*changes the withdrawal sign for the data that has repeated
 wells removed 

@author: Michael Getachew Tadesse

"""
import pandas as pd

dat = pd.read_csv("ecftx_tr_20190329_GLRSTA_Counties_removedRepWells.csv")
dat.drop('Unnamed: 0', axis = 1, inplace = True)

print(dat)

dat['withdrawal'] = dat['withdrawal'] * -1

print(dat)

dat.to_csv("ecftx_tr_20190329_GLRSTA_Counties_removedRepWells_reversedWithdrawal.csv")

