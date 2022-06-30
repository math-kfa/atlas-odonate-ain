# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 14:43:48 2021

@author: mathi
"""



import matplotlib
import matplotlib.pyplot as plt
from datetime import datetime
from sklearn.neighbors import KernelDensity
import matplotlib.dates as mdates

from shapely.geometry import Point
import numpy as np

import scipy.stats as sps
import plotly.express as px
import pandas as pd
import geopandas as gpd
import csv
from shapely.geometry import MultiLineString
from shapely.ops import polygonize
from geopandas.tools import sjoin
import seaborn as sns



#----------------------------------------------------------------------------------------------------
# imports
#----------------------------------------------------------------------------------------------------
# import csv
odo_data_csv = r'C:/Users/mathi/Documents/Biblio/Atlas_odonate_ain_2022/statistiques/grpls_01_2021_11_03_16_44_02_iso88591.csv'

# transform in dataframe
df = pd.read_csv(
                'grpls_01_2021_11_03_16_44_02_iso88591.csv', 
                 encoding = "ISO-8859-1", 
                 sep=';',
                 low_memory=False,
                 )
                 
# convert date to dateframe
df['date_obs'] = pd.to_datetime(df['date_obs'], dayfirst=True, yearfirst=False, format='%d/%m/%Y')
# select only some columns
df = df[['date_obs','nom_latin','stade']]




#----------------------------------------------------------------------------------------------------      
#  arrange dataframe
#----------------------------------------------------------------------------------------------------
# filter after 2000


#filt = ((df['date_obs']>='2000') & (df['stade'] != 'larve') & (df['stade'] != 'exuvie') & (df['stade'] != 'mort-'))


#apply filter
df = df.loc[(df['date_obs']>='2000') & (df.stade.astype(str) != 'larve') | (df.stade.astype(str) != 'exuvie') | (df.stade.astype(str) != 'mort-')]



pd.set_option('display.max_rows', 500)
print(df)

# set index
df.set_index('date_obs')
#extract days
df['day'] = pd.DatetimeIndex(df['date_obs']).day
# extract month
df['month'] = pd.DatetimeIndex(df['date_obs']).month
# only day & month
df['DM'] = df['date_obs'].apply(lambda x: x.strftime('%d-%m'))
 

# week
df['week'] = df['date_obs'].apply(lambda x:"%d" % (x.week))
# convert to int
df['week'] = df['week'].astype(int) 

pd.set_option('display.max_rows', 500)
print(df)



#----------------------------------------------------------------------------------------------------
#  generating list of species (unique name)
#----------------------------------------------------------------------------------------------------
# list of unique value
species = pd.unique(df['nom_latin']).tolist()
# select only species 
species = [val for val in species if not val.endswith(("sp.","ae","donata","ptera"))]


    


#----------------------------------------------------------------------------------------------------
#  for 1 species
#----------------------------------------------------------------------------------------------------
# select the serie for a specie
y = df.loc[df.nom_latin=='Aeshna affinis']
x = df.loc[df.nom_latin=='Aeshna affinis', ['week']]
z = df.loc[df.nom_latin=='Aeshna affinis', ['month']]
# print all rows
pd.set_option('display.max_rows', x.shape[0]+1)
print(x.sort_values(['week'], ascending=False))

# plot date range



#ax = x.plot.hist(bins=52, legend=False)
ax = z.plot.hist(bins=12, legend=False)



 
# visualizing plot using matplotlib.pyplot library


#f, ax = plt.subplots(1)
plt.xlim(0, 52)

plt.xlabel('Date observation')
plt.ylabel('Nombre observations')
plt.show()



# https://stackoverflow.com/questions/11315641/python-plotting-a-histogram-with-a-function-line-on-top


#----------------------------------------------------------------------------------------------------
#  for all species
#----------------------------------------------------------------------------------------------------
# loop
'''
for specie in species:
    specie = df.loc[df.nom_latin==specie, ['date_obs']]
    specie.groupby([specie["date_obs"].dt.month]).count().plot(kind="bar")
'''


