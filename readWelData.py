import re
import pandas as pd

######################################################
# open and read file
file = open('ecftx_tr.20190329.wel')
content = file.readlines()
# newContent = content[3:]
r1 = content[2688335]
r2 = content[2688336]
print(r1)
print(r2)
print(r2.split()[0])
print(r1.split()[0] == "116883")
# splitStr = newContent.split()
# print(splitStr[4]+splitStr[5]+splitStr[6])
# dd = pd.DataFrame(newContent)

# print(dd)


# # to find rows where stress period changes
# getPeriod = lambda x: "STRESS PERIOD" in x

# periodBool = list(map(getPeriod, dd[0]))
# # print(dd[periodBool])

# ######################################################
# # find where the stress period years are located
# stressDat = dd[periodBool]
# stressDat.reset_index(inplace = True)
# # print(stressDat)
# # print(stressDat)
# # print(dd[0][stressDat['index']])
# index = stressDat['index']
# # print(index)
# ######################################################

# ######################################################
# # create new dataframe for stress periods
# dfStressPeriod = pd.DataFrame(columns= ['index', 'stressPeriod'])

# # get the stress period years
# for sp in index:
#     # print(dd[0][sp])
#     spDf = dd[0][sp]
#     spDat = re.split('\s+', spDf)
#     # print(spDat[5] + "-" + spDat[6])
#     newStressPeriod = pd.DataFrame([sp, spDat[5] + "-" + spDat[6]]).T
#     newStressPeriod.columns = ['index', 'stressPeriod']
#     dfStressPeriod = pd.concat([dfStressPeriod, newStressPeriod], axis = 0)

# # print(dfStressPeriod)
# ######################################################



# # ########################################################################
# # create a new dataframe
# df = pd.DataFrame(columns= \
#     ['index', 'layer', 'row', 'columns', 'withdrawal', 'name', 'remark', 'stressPeriod'])
# # ########################################################################


# stressPeriod = dfStressPeriod[dfStressPeriod['index'] == 0]['stressPeriod']
# print(stressPeriod)

# for i in range(len(newContent)):
#     print(newContent[i])

#     if i in dfStressPeriod['index']:
#         stressPeriod = dfStressPeriod[dfStressPeriod['index'] == i]['stressPeriod']
#         continue
    
#     newDat = re.split('\s+', newContent[i])
#     newDf = pd.DataFrame([newDat, stressPeriod]).T
#     newDf.columns = ['index', 'layer', 'row', 'columns', 'withdrawal', 'name', 'remark', 'stressPeriod']
#     print(newDf)
#     df = pd.concat([df, newDf], axis = 0)

# print(df)


# # newDat.to_csv("outfile.csv")
