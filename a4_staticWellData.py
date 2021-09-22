import pandas as pd

dat = pd.read_csv("ecftx_tr_20190329_stressPeriod_v2.csv")


# convert row and col to string
toStr = lambda x : str(x)

dat['row'] = pd.DataFrame(list(map(toStr, dat['row'])))
dat['columns'] = pd.DataFrame(list(map(toStr, dat['columns'])))
dat['year'] = pd.DataFrame(list(map(toStr, dat['year'])))


dat['monYear'] = dat['mon'] + dat['year']

dat['rowColPermit'] = dat['row'] + "_" + dat['columns']+ "_" + dat['name']

print(dat)

for ii in range(len(dat)):
    if len(dat[(dat['rowColPermit'] == dat['rowColPermit'][ii])]) > 1:
        print("multiple wells")

