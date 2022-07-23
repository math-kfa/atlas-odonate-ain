# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 14:43:48 2021

@author: Mathias Kalfayan
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib.ticker as plticker


#----------------------------------------------------------------------------------------------------
# imports
#----------------------------------------------------------------------------------------------------
# import csv
odo_data_csv = r'C:/Users/mathi/Documents/Biblio/Atlas_odonate_ain_2022/statistiques/grpls_01_2021_11_03_16_44_02_iso88591.csv'
outdir = 'C:/Users/mathi/Documents/Biblio/Atlas_odonate_ain_2022/statistiques/out_vol/'
month = ["Janvier", "Février", "   Mars  ", "  Avril  ", "   Mai   ", "  Juin  ", "Juillet", "   Août   ", "Septembre", " Octobre ", "Novembre", "Decembre"]

# transform in dataframe
df = pd.read_csv(
                odo_data_csv, 
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

#define filters

filt = ((df['date_obs']>='1950-01-01') & (df['stade'] != 'larve') & (df['stade'] != 'exuvie') & (df['stade'] != 'mort-') & (df['stade'] != '-mort'))
#filt = df[(~df['stade'].isin(["larve", "exuvie", "mort-", "-mort"])) & (df['date_obs'] >= '2000-01-01')] # other syntax

#apply filters
df = df.loc[filt]

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

# print df to verify 
#pd.set_option('display.max_rows', 500)
#print(df)



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
sp = df.loc[df.nom_latin=='Somatochlora arctica']
# print all rows
pd.set_option('display.max_rows', sp.shape[0]+1)
#print(sp.sort_values(['week'], ascending=False))

#############################################################################

#min and max week value
minWeek = sp['week'].min()
maxWeek = sp['week'].max()


minDateIndex = df.index[sp['week'].min()]
maxDateIndex = df.index[sp['week'].max()] #.tolist() # => .tolist seems not useful
print("indexes", minDateIndex, maxDateIndex)

print(sp.iloc[1,:])

print("CORRESPONDING ROW ? :")
#print(sp.iloc["date_obs", minDateIndex])

# minDate = 
# maxDate = 


# plot
fig , ax1 = plt.subplots(1, 1, figsize=(12, 6), dpi=100)
ax2 = ax1.twiny()
ax2 = sp['week'].plot(kind='hist', ax=ax2, secondary_y=False, bins=52, legend=False, color='#7d0f51')
sp['week'].plot(kind='kde', ax=ax2, secondary_y=True, legend=False, color='orange')

#axes range
ax2.set_xlim(0, 52)
ax1.set_xlim(0, 12)




ax2.annotate(minWeek,
             xy = (sp['week'].min()-2, 2),
             xytext=(30, 30), 
             textcoords='offset points',
             arrowprops=dict(arrowstyle='-|>'))

ax2.annotate(maxWeek,
             xy = (sp['week'].max() +2, 2),
             xytext=(30, 30), 
             textcoords='offset points',
             arrowprops=dict(arrowstyle='-|>'))



##############################################################################



# axes' number of bins
plt.locator_params(axis='x', nbins=30)
ax1.set_xticks(np.arange(0, 12))
# axes' labels
ax1.set_xticklabels(month, rotation=45, ha='left', minor=False)
#ax1.set_ylabel('Densité')
#ax1.set_xlabel('Mois')
ax2.set_xlabel('Semaine')
ax2.set_ylabel('Nombre observations')
ax1.xaxis.grid(linestyle='--')
plt.show()



#----------------------------------------------------------------------------------------------------
#  for all species
#----------------------------------------------------------------------------------------------------
# loop
'''
for specie in species:
    specie = df.loc[df.nom_latin==specie, ['date_obs']]
    specie.groupby([specie["date_obs"].dt.month]).count().plot(kind="bar")
'''


