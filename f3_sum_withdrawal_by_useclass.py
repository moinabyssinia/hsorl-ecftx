"""  
Updated on Wed Sep 02 14:53:00 2022

sum withdrawals based on use class
and stress period (year)

@author: Michael Getachew Tadesse

"""
import os 
import re
import pandas as pd


dir_home = 'R:\\40715-013 UKFPLOS\\Data\\H&H_Data\\GW\\'\
                'ecftx_files\\extracted_from_wel_file'

os.chdir(dir_home)

dat = pd.read_csv('ecftxPermitsAll.csv')


print(dat)

uc = dat['use_class'].unique()
yr = dat['year'].unique()

print(uc)
print(yr)

# empty dataframe
withdrawal = pd.DataFrame(columns = ['uc', 'year', 'total_withdrawal'])


for uu in uc:
    for yy in yr:
        df = dat[(dat['use_class'] == uu) & (dat['year'] == yy)]
        sum_withd = df['withdrawal'].sum()

        print(uu, yy, sum_withd)

        new_df = pd.DataFrame([uu, yy, sum_withd]).T
        new_df.columns = ['uc', 'year', 'total_withdrawal']

        withdrawal = pd.concat([withdrawal, new_df], axis = 0)



withdrawal.to_csv('all_ECFTX_wells_withdrawal_sum_by_use_class.csv')