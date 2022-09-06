"""  
Updated on Tue Sep 06 10:31:00 2022

filter ukb wells that are PWS

@author: Michael Getachew Tadesse

"""
import os 
import pandas as pd

dir_home = 'R:\\40715-013 UKFPLOS\\Data\\H&H_Data\\GW\\ecftx_files\\ukb_pumping_wells'

os.chdir(dir_home)

dat = pd.read_csv('ukb_ecftx_GW_no_DSS_wells.csv')

print(dat)

print(dat[dat['use_class'] == 'PS'])

dat_ps = dat[dat['use_class'] == 'PS']
dat_ps['id'] = dat_ps.row.astype(str).str.cat(dat_ps['columns'].astype(str), \
                            sep = "_") + "_"  + dat_ps['layer'].astype(str) + "_" + dat_ps['name']



dat_ps.to_csv('ukb_ecftx_GW_PS_wells.csv')