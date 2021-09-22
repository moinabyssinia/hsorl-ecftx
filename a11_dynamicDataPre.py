"""
Created on Wed Aug 25 18:29:00 2021

this program:
*filters the withdrawal time series for each rowColPermit

@author: Michael Getachew Tadesse

"""
import os
import pandas as pd

dirHome = "C:\\Users\\mi292519\\Documents\\hazenStuff\\byCounty"
dirOut = "C:\\Users\\mi292519\\Documents\\hazenStuff\\byCounty4Dfs0"


os.chdir(dirHome)

countyList = os.listdir()

for county in countyList:
    os.chdir(dirHome)

    print(county)

    dat = pd.read_csv(county)
    dat.drop('Unnamed: 0', axis = 1, inplace = True)

    # modify month and year format
    getStr = lambda x : str(int(x))
    dat['year'] = pd.DataFrame(list(map(getStr, dat['year'])))
    dat['date'] = dat['mon'] + "-" + dat['year']

    print(dat)

    # print(dat[['monYear', 'rowColPermit', 'withdrawal']])

    rcpUnique = dat['rowColPermit'].unique()
    # print(rcpUnique)


    dfs0File = pd.DataFrame(dat['date'].unique())
    dfs0File.columns = ['date']

    for rcp in rcpUnique:
        df = dat[dat['rowColPermit'] == rcp]
        newDf = df[['date', 'withdrawal']]
        newDf.columns = ['date', rcp]
        # print(newDf)

        # merge to rcpUnique
        dfs0File = pd.merge(dfs0File, newDf, on="date", how="left")

    print(dfs0File)

    # save county dfs0 ready csv
    os.chdir(dirOut)
    dfs0File.to_csv(county)