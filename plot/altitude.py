# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 14:43:48 2021

@author: Mathias Kalfayan
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
from matplotlib.ticker import MaxNLocator
import matplotlib.ticker as ticker
from matplotlib.ticker import FormatStrFormatter



#----------------------------------------------------------------------------------------------------
#imports
#----------------------------------------------------------------------------------------------------
# import csv
odo_data_csv = r'C:/Users/mathi/Documents/Biblio/Atlas_odonate_ain_2022/carto/grpls_01_2021_11_03_16_44_02_iso88591.csv'
outdir = 'C:/Users/mathi/Documents/Biblio/Atlas_odonate_ain_2022/statistiques/out_vol/'

# transform in dataframe
df = pd.read_csv(odo_data_csv,  
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
plt.savefig(outdir+'Orthetrum coerulescens'+'.png')
plt.show()

'''




#----------------------------------------------------------------------------------------------------
#  for all species
#----------------------------------------------------------------------------------------------------
# loop
for specie in species:
    specie = df.loc[df.nom_latin==specie, ['nom_latin','altitude']]
    # plot(800x600)
    plt.figure(figsize=(8, 6), dpi=100)
    specie.plot(
                  kind='hist',
                  grid=False,
                  legend=False,
                  bins=50,
                  color='#7d0f51')
    #set axes parameters
    #plt.ylim(0.9)
    #plt.gca().yaxis.set_major_formatter(FormatStrFormatter('%.0f'))
    plt.xlabel('Altitude')
    plt.ylabel('Nombre observations')
    #save
    title = (pd.unique(specie['nom_latin']))
    #plt.savefig(outdir+str(title)+'.png')
    plt.show()







