import os
import pandas as pd

dirHome = "C:\\Users\\mtadesse\\Hazen and Sawyer\\MIKE_Modeling_Group - Documents\\"\
        "ECFTX\\extractedWellData\\011-allECFTXPermits-county-useclass\\analysis\\"\
                "rawFile"

os.chdir(dirHome)

dat = pd.read_csv("ecftx_clipped_v4_removedRepWells_with_traversingWells.csv")

print(dat)

print(dat['id'].unique())
print(len(dat['id'].unique()))
print(len(dat['id']))