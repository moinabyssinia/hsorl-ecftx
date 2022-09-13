"""
Created on Mon Sep 12 17:04:00 2021

this program:
*aggregates the withdrawal of wells by cell

@author: Michael Getachew Tadesse
"""

import os
import numpy as np
import pandas as pd


dir_home = 'R:\\40715-013 UKFPLOS\\Data\\H&H_Data\\GW\\ecftx_files\\ukb_pumping_wells\\to_Jeremy\\merged_100m\\rib'

os.chdir(dir_home)
dat = pd.read_csv('rib_wells_100_mesh_data_with_cell.csv')

# id column is only for the PWS wells
dat = dat[['x_utm_m', 'y_utm_m', 'layer', 'ecftx_row', 'ecftx_columns',
       'withdrawal', 'name', 'mon', 'year', 'county', 'use_class', 'cell']]

dat['monyear'] = dat['mon'] + dat['year'].astype(str)


print(dat)
print(dat.columns)

# unique cell values
unq_cell = dat['cell'].unique()
print(len(unq_cell))

# unique monyear
unq_date = dat['monyear'].unique()
print(unq_date)


# create empty dataframe
df = pd.DataFrame(columns = ['x_utm_m', 'y_utm_m', 'layer',
       'name', 'mon', 'year', 'withdrawal', 'use_class', 'id', 'cell'])


isFirst = True
for cc in unq_cell:
    for my in unq_date:
        print(cc, my)
        newDf = dat[(dat['monyear'] == my) & (dat['cell'] == cc)]
        newDf.reset_index(inplace = True)

        x = newDf['x_utm_m'][0]
        y = newDf['y_utm_m'][0]
        layer = newDf['layer'][0]
        name = newDf['name'][0]
        mon = newDf['mon'][0]
        year = newDf['year'][0]
        use_class = newDf['use_class'][0]
        # id = newDf['id'][0]
        cell = newDf['cell'][0]

        withdrawal = newDf['withdrawal'].sum()


        newDF2 = pd.DataFrame([x, y, layer, name, mon, year, withdrawal, use_class, cell]).T
        newDF2.columns = ['x_utm_m', 'y_utm_m', 'layer', 'name', 'mon', 'year', 'withdrawal',
                                'use_class', 'cell']
        
        # print(newDF2)


        if isFirst:
            df = newDF2
            isFirst = False
        else:
            df = pd.concat([df, newDF2], axis = 0)


# save output
df.to_csv('rib_wells_100_mesh_summed_withdrawal.csv')
            
                
                


