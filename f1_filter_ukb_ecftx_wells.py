"""  
Updated on Wed Sep 02 11:19:00 2022

filter ukb wells from ecftx

@author: Michael Getachew Tadesse

"""
import os 
import re
import pandas as pd

dir_home = 'R:\\40715-013 UKFPLOS\\Data\\H&H_Data\\GW\\ecftx_files\\extracted_from_wel_file'

os.chdir(dir_home)


ecftx_all = pd.read_csv('ecftxPermitsAll.csv')
ecftx_clipped = pd.read_csv('ecftx_ukb_clipped.csv')
ecftx_clipped_gw = ecftx_clipped[ecftx_clipped['WD_TYPE'] == 'GW']

# print(ecftx_all)
print(ecftx_clipped_gw)


# print(ecftx_clipped.DISTPRMTST)
clipped_names = ecftx_clipped_gw.DISTPRMTST.tolist()
# print(clipped_names)

ukb_ecftx_GW = ecftx_all[ecftx_all['name'].isin(clipped_names)]

print(ukb_ecftx_GW['name'].unique())
print(len(ukb_ecftx_GW['name'].unique()))


# ukb_ecftx_GW.to_csv('ukb_ecftx_GW_wells.csv')

ukb_ecftx_GW_no_DSS = ukb_ecftx_GW[ukb_ecftx_GW['use_class'] != 'DSS']

ukb_ecftx_GW_no_DSS.to_csv('ukb_ecftx_GW_no_DSS_wells.csv')
