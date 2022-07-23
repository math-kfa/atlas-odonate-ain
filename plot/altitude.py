# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 14:43:48 2021

@author: Mathias Kalfayan
"""



import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.ticker as ticker



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


#----------------------------------------------------------------------------------------------------
#  for 1 species
#----------------------------------------------------------------------------------------------------
# select a species
sp = df.loc[df.nom_latin=='Orthetrum coerulescens', ['nom_latin','altitude']]
# plot(800x600)
plt.figure(figsize=(8, 6), dpi=100)
sp.plot( kind='hist',
        grid=False,
        legend=False,
        bins=50,
        color='deeppink')
# axes' labels  
plt.xlabel('Altitude')
plt.ylabel('Nombre observations')
plt.savefig(outdir+'Orthetrum coerulescens'+'.png')
plt.show()


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
    # axes' parameters for small df
    if len(specie) < 2:
        print("single value")
        plt.gca().xaxis.set_major_locator(ticker.MultipleLocator(1))
        plt.gca().yaxis.set_major_locator(ticker.MultipleLocator(1))
    # axes' labels       
    plt.xlabel('Altitude')
    plt.ylabel('Nombre observations')
    # save
    title = (pd.unique(specie['nom_latin']))
    plt.savefig(outdir+str(title)+'.png')
    plt.show()
