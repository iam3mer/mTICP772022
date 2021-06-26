# from os import read
import json
import pandas as pd
import numpy as np
import requests
import math

respuesta = requests.get('http://citibikenyc.com/stations/json')
# dataDF = pd.DataFrame(json.loads(respuesta.content))
dataDF = json.loads(respuesta.content)
dataDF = pd.DataFrame(dataDF['stationBeanList'])
# print(dataDF.columns)

dataDF = dataDF.loc[:,['stationName', 'availableDocks', 'totalDocks', 'availableBikes']]

# dataDF['availableDocks'][1] = np.nan

# print(dataDF['availableDocks'].notna())
# print(dataDF.availableDocks.notna())

# dataDF = dataDF[dataDF['availableDocks'].notna()]

# newRegister = dataDF.iloc[5,:]

# dataDF = dataDF.append(newRegister)

# dataDF['availableDocks']['Park Ave & St Edwards St'] = 56

# dataDF.drop_duplicates(['stationName'], inplace=True)

# dataDF.drop(['availableBikes'], axis=1, inplace=True)

# dataDF.drop([0], inplace=True)

unicos_availableDocks = set(dataDF['availableDocks'].unique())
unicos_totalDocks = set(dataDF['totalDocks'].unique())
unicos = list(unicos_availableDocks.union(unicos_totalDocks))

# print(dataDF.dropna(how='all'))

# dataDF.index = dataDF['stationName']
dataDF.set_index('stationName', inplace=True)

# print(dataDF['totalDocks']['Atlantic Ave & Fort Greene Pl'])

# dataDF['totalDocks'] = dataDF['totalDocks'].apply(lambda x: math.sqrt(x))
dataDF['totalDocks'] = dataDF['totalDocks'].apply(math.sqrt)

total = dataDF['availableDocks'].sum()
print(total)
# print(dataDF)

# --------------------------
dataDF = pd.read_json('http://citibikenyc.com/stations/json')
dataDF = pd.DataFrame(dict(dataDF['stationBeanList']))
# print(dataDF.loc['totalDocks',:])
dataDF.loc['totalDocks',:] = dataDF.loc['totalDocks',:].apply(math.sqrt)
total = dataDF.loc['availableDocks',:].sum()
print(total)

# dataDF = dataDF.transpose()
# print(dataDF)