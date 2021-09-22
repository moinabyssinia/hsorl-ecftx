"""
Created on Tue Aug 24 22:06:00 2021

this program:
*appends the counties for each well (row-col combination) 

@author: Michael Getachew Tadesse

"""

import pandas as pd

dat = pd.read_csv("ecftx_tr_20190329_GLRSTA.csv")

getStr = lambda x : str(x)

rowStr = pd.DataFrame(list(map(getStr, dat['row'])))
colStr = pd.DataFrame(list(map(getStr, dat['columns'])))

dat['rowcol'] = rowStr + "_" + colStr

print(dat)

datCounty = pd.read_csv("county_domain.csv")

print(datCounty)


# merge to get county names
datCountyClean = datCounty[['ROWCOL', 'County']]
datCountyClean.columns = ['rowcol', 'county']

print(datCountyClean)

datMergedCounty = pd.merge(dat, datCountyClean, on= 'rowcol', how="left")
print(datMergedCounty)

datMergedCounty.to_csv("ecftx_tr_20190329_GLRSTA_Counties.csv")