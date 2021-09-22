import re
import pandas as pd

# open and read file
file = open('ecftx_tr.20190329.wel')
content = file.readlines()

print(len(content))

# create a new dataframe
df = pd.DataFrame(columns= \
    ['layer', 'row', 'columns', 'withdrawal', 'name', 'stressPeriod'])

for ii in range(3,200000):
    print(ii)
    rowDat = content[ii].split()
    # print(rowDat)
    if (rowDat[0] == "116883"):
        stressPeriod = rowDat[4] + '-' + rowDat[5] + '-' + rowDat[6]
        # print(stressPeriod)
    else:
        newDf = pd.DataFrame([rowDat[0],rowDat[1], rowDat[2],rowDat[3],rowDat[4], stressPeriod]).T
        newDf.columns = ['layer', 'row', 'columns', 'withdrawal', 'name', 'stressPeriod']
        df = pd.concat([df, newDf], axis = 0)
    
print(df)
df.to_csv("test.csv")