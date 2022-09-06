

import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


os.chdir('R:\\40715-013 UKFPLOS\\Data\\H&H_Data'\
                '\\GW\\ecftx_files\\extracted_from_wel_file')



dat = pd.read_csv("ukb_ecftx_GW_no_DSS_wells.csv")


print(dat)

# get unique values of layers
print(dat['layer'].unique())

# print(dat.columns)

# print(dat.name.unique())

# test = dat[dat['name'] == 'cen_Lake_11432']

# print(test.head(50))

# print(dat.shape)

# print(dat.columns)

# print(len(dat.name.unique()))

# print(dat.use_class.unique())


# testDat = dat[dat['year'] == 2011]
# testDat.to_csv('ecftx_all_wells.csv')

# print(dat[dat['year'] == 2011])
# print(dat[dat['year'] == 2005])
# print(dat[dat['year'] == 2013])
# print(dat[dat['year'] == 2004])

