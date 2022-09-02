"""  
Updated on Wed Sep 02 09:59:00 2022

Read .wel data 

@author: Michael Getachew Tadesse

"""
import os 
import re
import pandas as pd

dir_home = 'D:\\MIKE_Modeling_Files\\Hazen and Sawyer\\MIKE_Modeling_Group - Documents\\GLRSTA\\data\\ECFTX\\extractedWellData'

dir_out = 'D:\\MIKE_Modeling_Files\\Hazen and Sawyer\\MIKE_Modeling_Group - Documents\\GLRSTA\\data\\ECFTX\\extractedWellData\\01-rawFiles'

# open and read file
os.chdir(dir_home)
file = open('ecftx_tr.20190329.wel')
content = file.readlines()

print(len(content))

# create a new dataframe
df = pd.DataFrame(columns= \
    ['layer', 'row', 'columns', 'withdrawal', 'name', 'stressPeriod'])

for ii in range(3,len(content)):
    rowDat = content[ii].split()
    print(rowDat)
    if (rowDat[0] == "116883"):
        stressPeriod = rowDat[4] + '-' + rowDat[5] + '-' + rowDat[6]
        print(stressPeriod)
    else:
        newDf = pd.DataFrame([rowDat[0],rowDat[1], rowDat[2],rowDat[3],rowDat[4], stressPeriod]).T
        newDf.columns = ['layer', 'row', 'columns', 'withdrawal', 'name', 'stressPeriod']
        df = pd.concat([df, newDf], axis = 0)
    
print(df)


os.chdir(dir_out)
df.to_csv("ecftxWellDataCleaned_090222.csv")