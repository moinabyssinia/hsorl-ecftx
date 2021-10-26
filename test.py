import os
import pandas as pd

dirHome = "C:\\Users\\mtadesse\\Hazen and Sawyer\\MIKE_Modeling_Group - Documents\\"\
                "ECFTX\\extractedWellData\\011-allECFTXPermits-county-useclass\\"\
                                "exportdFromShp"

os.chdir(dirHome)

dat = pd.read_csv("ecftx_clipped_v4.txt")
dat.drop(['FID', 'field_1'], axis = 1, inplace = True)

# get unique name
# getName = lambda x: (x['row'])  + x['name']

# dat['rowcolname'] = pd.DataFrame(list(map(getName, dat)))

dat['rowcolname'] = dat.row.astype(str).str.cat(dat['columns'].astype(str), sep = "_") + "_" + dat['name']
print(dat)

# print unique wells
print(dat['rowcolname'].unique())
print(len(dat['rowcolname'].unique()))