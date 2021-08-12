#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 18:46:36 2021

Projection of Boston Red Sox win percentage at the end of the season based on 
pythagorean expectation and game-by-game results as of 7:00 PM on Monday, 8/9

@author: YouCanCallMeAll
"""

# %% 1. Import modules
import pandas as pd
import matplotlib.pyplot as plt

# %% 2. Import data
data = pd.read_csv(r'/Users/YouCanCallMeAll/Desktop/Baseball/wp001-sox_proj_wpct/data/sox_game_results.csv')
print(data.head())
for col in data.columns:
    print(col)

# %% Create filtered dataset to only include data from played games
gp_data = data[data['gp_indc'] == 'boxscore']
#print(gp_data)

# %% Cleanse data
    
#rename columns
gp_data = gp_data.rename(columns={"Unnamed: 2": "gp_indc"})

#change data types
gp_data['m#'] = gp_data['m#'].astype(int)
gp_data['R'] = gp_data['R'].astype(int)
gp_data['RA'] = gp_data['RA'].astype(int)

#print(gp_data.head())
#for col in gp_data.columns:
#    print(col)

# %% Create cumulative sums of runs scored and runs allowed
gp_data['cumsum_rs'] = gp_data['R'].cumsum()
gp_data['cumsum_ra'] = gp_data['RA'].cumsum()

print(gp_data.head())
for col in gp_data.columns:
    print(col)

# %% Plot cumulative runs scored and cumulative runs allowed across games played
plt.plot(gp_data['m#'], gp_data['cumsum_rs'], color='#0C2340')
plt.plot(gp_data['m#'], gp_data['cumsum_ra'], color='#BD3039')
plt.legend(['Runs Scored', 'Runs Allowed'])
plt.show()

# %% Plot cumulative vs scored and cumulative runs allowed across games played
plt.plot(gp_data['cumsum_ra'], gp_data['cumsum_rs'], color='#0C2340')
plt.show()

# %% Plot runs scored versus runs allowed across games played
plt.scatter(gp_data['RA'], gp_data['R'], color='#0C2340')
plt.show()

# %% Calculate total runs, runs allowed, and games played YTD
    
#calculate runs scored and save to variable 'rs'
rs = pd.to_numeric(gp_data['R']).sum()
#print(rs)

#calculate runs allowed and save to variable 'ra'
ra = pd.to_numeric(gp_data['RA']).sum()
#print(ra)

gp = gp_data['gp_indc'].count()
#print(gp)

# %% Calculate current pythagorean win expectation
exp = 1.85

wpct = (rs ** exp) / ((rs ** exp) + (ra ** exp))
print(wpct)

# %% Project runs scored and runs allowed for whole season arithmatically
gt = 162

rs_proj = (rs / gp) * gt
ra_proj = (ra / gp) * gt
print(rs_proj, ra_proj)

# %% Calculate current pythagorean win expectation with projected figures
exp = 1.85

wpct = (rs_proj ** exp) / ((rs_proj ** exp) + (ra_proj ** exp))
print(wpct)
# there was no differene between actual and projected wpct
