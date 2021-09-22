"""
Created on Sat Aug 24 08:00:00 2021

this program:
*filters out the well data to match the model domain 

@author: Michael Getachew Tadesse

"""


import pandas as pd

dat = pd.read_csv("ecftx_tr_20190329_SJR_SF.csv")
dat.drop(['Unnamed: 0', 'Unnamed: 0.1'], axis = 1, inplace = True)
print(dat)

# subset the well files inside the model domain rectangle
"""  
NE: 371_740
NW: 371_547
SE: 603_740
SW: 603_547
"""

datGLRSTA = dat[(dat['row'] >= 371) & (dat['row'] <= 630) &\
    (dat['columns'] >= 547) & (dat['columns'] <= 740)]

print(datGLRSTA)

datGLRSTA.to_csv("ecftx_tr_20190329_GLRSTA.csv")