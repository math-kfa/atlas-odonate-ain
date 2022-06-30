# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 14:43:48 2021

@author: mathi
"""



import matplotlib
import matplotlib.pyplot as plt

from sklearn.neighbors import KernelDensity

from shapely.geometry import Point
import numpy as np

import plotly.express as px
import pandas as pd
import geopandas as gpd
import csv
from shapely.geometry import MultiLineString
from shapely.ops import polygonize
from geopandas.tools import sjoin
import seaborn as sns



#----------------------------------------------------------------------------------------------------
#imports
#----------------------------------------------------------------------------------------------------
# import csv
odo_data_csv = r'C:/Users/mathi/Documents/Biblio/Atlas_odonate_ain_2022/carto/grpls_01_2021_11_03_16_44_02_iso88591.csv'
# transform in dataframe
df = pd.read_csv('grpls_01_2021_11_03_16_44_02_iso88591.csv',  
                 encoding = "ISO-8859-1", 
                 sep=';', 
                 low_memory=False)



 


#----------------------------------------------------------------------------------------------------
#  list of species
#----------------------------------------------------------------------------------------------------
# liste with unique value of species
species = pd.unique(df['nom_latin']).tolist()
# select only species 
species = [val for val in species if not val.endswith(("sp.","ae","donata","ptera"))]




'''
#----------------------------------------------------------------------------------------------------
#  for 1 species
#----------------------------------------------------------------------------------------------------
# select the serie x=specie
x = df.loc[df.nom_latin=='Orthetrum coerulescens', ['nom_latin','altitude']]
# plot altitude
plt.figure()
x.plot.hist(
                  grid=False,
                  legend=False,
                  bins=50,
                  color='deeppink')

plt.xlabel('Altitude')
plt.ylabel('Nombre observations')

'''





#----------------------------------------------------------------------------------------------------
#  for all species
#----------------------------------------------------------------------------------------------------
# loop
for specie in species:
    specie = df.loc[df.nom_latin==specie, ['nom_latin','altitude']]
    # plot
    plt.figure()
    specie.plot.hist(
                  grid=False,
                  legend=False,
                  bins=50,
                  color='deeppink')
    plt.xlabel('Altitude')
    plt.ylabel('Nombre observations')


    










