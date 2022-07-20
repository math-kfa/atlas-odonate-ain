# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 14:43:48 2021

@author: mathi
"""

import matplotlib.pyplot as plt
import pandas as pd


#----------------------------------------------------------------------------------------------------
# imports
#----------------------------------------------------------------------------------------------------
# import csv
odo_data_csv = r'C:/Users/mathi/Documents/Biblio/Atlas_odonate_ain_2022/statistiques/grpls_01_2021_11_03_16_44_02_iso88591.csv'
outdir = 'C:/Users/mathi/Documents/Biblio/Atlas_odonate_ain_2022/statistiques/out_vol/'

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


# df[(~df['stade'].isin(["larve", "exuvie", "mort-"])) & (df['date_obs'] >= '2000-01-01')]

#filt = ((df['date_obs']>='2000') & (df['stade'] != 'larve') & (df['stade'] != 'exuvie') & (df['stade'] != 'mort-'))

#df[df['date_obs'] >= '2000-01-01']
#df[~df['stade'].isin(["larve", "exuvie", "mort-"])]

#apply filter
df = df.loc[(df['date_obs']>='2000') & (df.stade.astype(str) != 'larve') | (df.stade.astype(str) != 'exuvie') | (df.stade.astype(str) != 'mort-')]
breakpoint()

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
y = df.loc[df.nom_latin=='Somatochlora arctica']
x = df.loc[df.nom_latin=='Somatochlora arctica', ['week']]
z = df.loc[df.nom_latin=='Anax imperator', ['date_obs']]
# print all rows
pd.set_option('display.max_rows', x.shape[0]+1)
print(y.sort_values(['week'], ascending=False))


#min and max value
print(y['date_obs'].min())
print(y['date_obs'].max())

print(y[y['date_obs']==y['date_obs'].min()])
print(y[y['date_obs']==y['date_obs'].max()])


# plot date range



'''
fig, ax1 = plt.subplots()
ax1.plot(x, x)
ax2 = ax1.twiny()
ax2.plot(x, )


plt.show()

# witch month given the week number = number of week * 7 / 30

'''



fig , ax1 = plt.subplots(1, 1, figsize=(10, 6), dpi=100)
ax2 = ax1.twiny()
#ax3 = ax1.twinx()
x.plot(kind='hist', ax=ax2, secondary_y=False, bins=52, legend=False, color='#7d0f51')
x.plot(kind='kde', ax=ax2, secondary_y=True, legend=False, color='orange')
#x.plot(kind='kde', ax=ax3, legend=False, color='orange')



# visualizing plot using matplotlib.pyplot library

ax2.set_xlim(0, 53)
ax1.set_xlim(0, 13)
ax1.set_xlabel('Date observation')
ax2.set_ylabel('Nombre observations')
plt.show()



#add secondary x axis
#https://stackoverflow.com/questions/10514315/how-to-add-a-second-x-axis-in-matplotlib



#----------------------------------------------------------------------------------------------------
#  for all species
#----------------------------------------------------------------------------------------------------
# loop
'''
for specie in species:
    specie = df.loc[df.nom_latin==specie, ['date_obs']]
    specie.groupby([specie["date_obs"].dt.month]).count().plot(kind="bar")
'''


