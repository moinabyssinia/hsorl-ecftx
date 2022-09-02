import os
import pandas as pd

dirHome = "C:\\Users\\mtadesse\\Hazen and Sawyer\\MIKE_Modeling_Group - Documents\\ECFTX\\"\
                "extractedWellData\\011-allECFTXPermits-county-useclass\\analysis\\concat_refinedWells"

os.chdir(dirHome)

dat = pd.read_csv("allWells_with_watershed_v2.csv")

print(dat)
print(dat.columns)

dat = dat[['id', 'date', 'x_utm_m', 'y_utm_m', 'layer', 'county',      
       'use_class', 'withdrawal', 'NAME']]

dat.columns = ['id', 'date', 'x_utm_m', 'y_utm_m', 'layer', 'county',      
       'use_class', 'withdrawal', 'watershed']

print(dat)

dat.to_csv("allWells_with_watershed_v2.csv")