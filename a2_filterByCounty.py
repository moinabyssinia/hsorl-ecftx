import os
import pandas as pd


dirHome = "C:\\Users\\mtadesse\\Hazen and Sawyer\\"\
        "MIKE_Modeling_Group - Documents\\cfwi-model-files\\"\
                "ECFTX_Calib\\ECFTX_Calib\\model\\extractedWellData"

os.chdir(dirHome)

# provide file
dat = pd.read_csv("test.csv")
dat.drop('Unnamed: 0', axis = 1, inplace = True)

unqNames = pd.DataFrame(dat['name'].unique())

print(len(unqNames))

print(dat[(dat['row'] == 208) & (dat['columns'] == 580)]) 


# by name
getCountyWell = lambda x: x.startswith("cen_Brev")

brevCounty = pd.DataFrame(list(map(getCountyWell, dat['name'])))

print(dat[brevCounty[0]].head(20))