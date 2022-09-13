"""
Created on Mon Sep 12 16:51:00 2021

this program:
*gets the cell_id of the well which is 
 merging ecftx well info with the 100m x 100m
 mesh 

@author: Michael Getachew Tadesse
"""

import os
import numpy as np
import pandas as pd


dir_home = 'R:\\40715-013 UKFPLOS\\Data\\H&H_Data\\GW\\ecftx_files\\wells_100m_mesh_data'
dir_pumping_wells = 'R:\\40715-013 UKFPLOS\\Data\\H&H_Data\\GW\\ecftx_files\\ukb_RIB_wells'

# mesh data
os.chdir(dir_home)
mesh_dat = pd.read_csv('wells_100_mesh_data.csv')
print(mesh_dat)


# wells data
# data used here is only for UKB
os.chdir(dir_pumping_wells)
pump_dat = pd.read_csv('ukb_RIB_wells.csv') 

print(pump_dat)

# # get layers 1, 2, 3
# # for RIBs there is only Layer 1
# pump_dat = pump_dat[(pump_dat['layer'] == 1) | (pump_dat['layer'] == 2) | (pump_dat['layer'] == 3)]



# print(pump_dat)
# print(pump_dat.columns)


# merging mesh with PWS/RIB

merged_dat = pd.merge(pump_dat,mesh_dat, on = 'name', how = 'left')

print(merged_dat)

os.chdir(dir_home)
merged_dat.to_csv('rib_wells_100_mesh_data_with_cell.csv')