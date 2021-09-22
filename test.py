import pandas as pd

dat = pd.read_csv("ecftx_tr_20190329_GLRSTA_Counties.csv")
dat.reset_index(inplace = True)
dat.drop(['Unnamed: 0', 'Unnamed: 0.1', 'index', 'level_0'], axis = 1, inplace = True)

# print(dat)
# print(len(dat['rowColPermit'].unique()))

# print(dat[dat['rowColPermit'] == '377_606_cen_Indi_10000'])
# print(dat[dat['rowColPermit'] == '377_606_cen_Indi_10000']['layer'].unique())


# check which rocolpermit is cutting through multiple layers
silo = []
for ii in range(len(dat)):
    print(ii)
    if(len(dat[dat['rowColPermit'] == \
            dat['rowColPermit'][ii]]['layer'].unique()) > 1):
        print(dat['rowcol'][ii], dat[dat['rowColPermit'] == \
            dat['rowColPermit'][ii]]['layer'].unique())
        silo.append(dat['rowColPermit'][ii])
print(pd.DataFrame(silo).unique())