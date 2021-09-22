"""
Created on Sat Aug 24 08:00:00 2021

this program:
*filters out swfwmd wells 

@author: Michael Getachew Tadesse
"""


import pandas as pd

dat = pd.read_csv("ecftx_tr_20190329_stressPeriod_v2.csv")


# convert row and col to string
toStr = lambda x : str(x)

dat['row'] = pd.DataFrame(list(map(toStr, dat['row'])))
dat['columns'] = pd.DataFrame(list(map(toStr, dat['columns'])))
dat['year'] = pd.DataFrame(list(map(toStr, dat['year'])))


dat['monYear'] = dat['mon'] + dat['year']

dat['rowColPermit'] = dat['row'] + "_" + dat['columns']+ "_" + dat['name']

# print(dat[dat['rowColPermit'] == "194_580_cen_Brev_430"])

# filter wells from the swfwmd
removeSWFWells = lambda x: not x.startswith("SW_")
sf_sjrWells = dat[list(map(removeSWFWells, dat['name']))]

print(sf_sjrWells)


sf_sjrWells.to_csv("ecftx_tr_20190329_SJR_SF.csv")