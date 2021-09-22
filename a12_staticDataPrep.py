"""
Created on Wed Aug 26 07:40:00 2021

this program:
*prepares the static file for the wells

@author: Michael Getachew Tadesse

"""
import os
import pandas as pd

dirHome = "C:\\Users\\mi292519\\Documents\\hazenStuff"
dirOut = "C:\\Users\\mi292519\\Documents\\hazenStuff\\staticFile"

# all wells data
datWells = pd.read_csv("ecftx_tr_20190329_GLRSTA_Counties_allWells.csv")
datWells.drop('Unnamed: 0', axis = 1, inplace = True)

print(datWells)
print(datWells['layer'].unique())


# all layers top/bottom data 
datInfo = pd.read_csv("ECFTX_allRC_layersTopBot.csv")


# get unique wells/rcps
rcpUnique = datWells['rowColPermit'].unique()

# create empty dataframe
df = pd.DataFrame(columns = ['wellID', 'x', 'y', 'level', 
     'wellField', 'top', 'bottom', 'depth', 'fraction', 'dfs0File', 'dfs0Item'])

# defining top and bottom of layers
layerDict = {
    '1' : ['L01_top_ft', 'L02_top_ft'],
    '3' : ['L03_top_ft', 'L04_top_ft'],
    '4' : ['L04_top_ft', 'L05_top_ft'],
    '5' : ['L05_top_ft', 'L06_top_ft'],
    '7' : ['L07_top_ft', 'L08_top_ft'],
    '3_4' : ['L03_top_ft', 'L05_top_ft'],
    '3_4_5' : ['L03_top_ft', 'L06_top_ft'],
    '4_5' : ['L04_top_ft', 'L06_top_ft']
}


for rcp in rcpUnique:
    print(rcp)

    rowcol = '_'.join([rcp.split("_")[0], rcp.split("_")[1]])
    
    wellID = rcp
    x = datInfo[datInfo['ROWCOL'] == rowcol]['Xcoord_UTM'].unique()[0]
    y = datInfo[datInfo['ROWCOL'] == rowcol]['Ycoord_UTM'].unique()[0]
    level = datInfo[datInfo['ROWCOL'] == rowcol]['L01_top_ft'].unique()[0]
    wellField = rcp
    
    # figure out top and bottom
    rcpLayer = datWells[datWells['rowColPermit'] == rcp]['layer'].unique()[0]

    t, b = layerDict[str(rcpLayer)]
    # print(t, "-", b)
    top = datInfo[datInfo['ROWCOL'] == rowcol][t].values[0]
    bottom = datInfo[datInfo['ROWCOL'] == rowcol][b].values[0]
    depth = level - bottom
    
    fraction = 1.0
   
    dfs0File = ''.join(datWells[datWells['rowColPermit'] \
            == rcp]['county'].unique()[0].split()).upper()+".dfs0"
    dfs0Item = rcp

    # print(wellID, "-", x, "-", y, "-", level, "-", top, "-", 
    #     bottom, "-", depth, "-", dfs0File, "-", dfs0Item)


    newDf = pd.DataFrame([wellID, x, y, level, wellField, top, 
        bottom, depth, fraction, dfs0File, dfs0Item]).T 
    newDf.columns = ['wellID', 'x', 'y', 'level', 
     'wellField', 'top', 'bottom', 'depth', 'fraction', 'dfs0File', 'dfs0Item']

    # add to empty dataframe
    df = pd.concat([df, newDf], axis = 0)

# save as csv
os.chdir(dirOut)
df.to_csv("staticWellFile.csv")

