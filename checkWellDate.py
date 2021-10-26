import os 
import pandas as pd

dirHome = "C:\\Users\\mtadesse\\Hazen and Sawyer\\"\
        "MIKE_Modeling_Group - Documents\\ECFTX\\extractedWellData\\01-rawFiles"
        

os.chdir(dirHome)

dat = pd.read_csv("ecftx_tr.20190329.csv")

print(dat)


print(dat[(dat['0'] == 1) & (dat['1'] == 507) &
            (dat['2'] == 680) & (dat['4'] == 'SF_56-02503-W_194084')])