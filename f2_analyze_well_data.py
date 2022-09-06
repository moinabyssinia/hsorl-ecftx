"""  
Updated on Wed Sep 02 14:09:00 2022

analyze ecftx well data

@author: Michael Getachew Tadesse

"""
import os 
import re
import pandas as pd


dir_home = 'R:\\40715-013 UKFPLOS\\Data\\H&H_Data\\GW\\ecftx_files\\extracted_from_wel_file'

os.chdir(dir_home)


dat = pd.read_csv('ukb_ecftx_GW_no_DSS_wells.csv')

print(dat)

print(dat.columns)

print(len(dat.name.unique()))
print(len(dat.use_class.unique()))

# print(dat[dat['year'] == 2005])
# print(dat.name.unique())

# print(dat.use_class.value_counts())

print(dat['withdrawal'].describe())