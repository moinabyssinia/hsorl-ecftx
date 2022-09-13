"""
Created on Wed Aug 25 18:29:00 2021
modified on Tue Sep 06 11:15:00 2022
modified on Tue Sep 13 11:08:00 2022

this program:
*filters the withdrawal time series for each cell_id and
 prepares it on a format that is needed for dfs0

@author: Michael Getachew Tadesse

"""
import os
import pandas as pd


dirHome = "R:\\40715-013 UKFPLOS\\Data\\H&H_Data\\GW\\ecftx_files\\ukb_pumping_wells\\to_Jeremy\\merged_100m\\rib"
dirOut = "R:\\40715-013 UKFPLOS\\Data\\H&H_Data\\GW\\ecftx_files\\ukb_pumping_wells\\to_Jeremy\\merged_100m\\rib\\dynamic_data_100m"


os.chdir(dirHome)

dat = pd.read_csv('rib_wells_100_mesh_summed_withdrawal.csv')
print(dat)

# replace "AVE" with "DEC"
dat['mon'] = dat['mon'].str.replace('AVE', 'DEC')

# concatenate mon and year
removeExt = lambda x: str(x).split('.0')[0]
dat['year'] = pd.DataFrame(list(map(removeExt, dat['year'])))
dat['date'] = pd.DataFrame(pd.to_datetime(dat['year'].astype(str) + dat['mon'].astype(str), 
                                             format = "%Y%b"))
# modify month and year format
dat['date'] = pd.to_datetime(dat['date'])

####################################################
# get only 2011 and 2014 data
dat = dat[((dat['date'] >= '2011-01-01') & (dat['date'] <= '2011-12-01')) |
                    ((dat['date'] >= '2014-01-01') & (dat['date'] <= '2014-12-01'))]
####################################################


# ####################################################
# # take just layers 1 and 2
# dat = dat[(dat['layer'] == 1) | (dat['layer'] == 2)]
# ####################################################



#################################################
# convert cubic feet/day to gallon/day
# withdrawal is in cfd; 1 cf = 7.48052 gallon
# multiplying by -1 
dat['withdrawal_gal'] = dat['withdrawal']*7.48052*-1
#################################################

rcpUnique = dat['cell'].unique()
# print(rcpUnique)
# print(len(rcpUnique))


dfs0File = pd.DataFrame(dat['date'].unique())
dfs0File.columns = ['date']

for rcp in rcpUnique:
    df = dat[dat['cell'] == rcp]
    newDf = df[['date', 'withdrawal_gal']] # take the gallon/day data
    newDf.columns = ['date', 'gallon_per_day']
    print(newDf)

    # merge to rcpUnique
    dfs0File2 = pd.merge(dfs0File, newDf, on="date", how="left")

    # print(dfs0File2)

    # save dfs0 ready csv
    os.chdir(dirOut)
    dfs0File2.to_csv(rcp + ".csv")