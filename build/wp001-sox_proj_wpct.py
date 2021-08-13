#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 18:46:36 2021

Projection of Boston Red Sox win percentage at the end of the season based on 
pythagorean expectation and game-by-game results as of Thursday, 8/11

@author: YouCanCallMeAll
"""

# %% 1. Import modules
import os,sys
import pandas as pd
pd.options.mode.chained_assignment = None  # default='warn'
import matplotlib.pyplot as plt

# %% 2. Import data
fileDir = os.path.abspath(os.path.dirname(sys.argv[0]))
data = pd.read_csv(fileDir + r'/../data/sox_game_results.csv')
print(data.head())

# %% Cleanse data
# Rename columns
data = data.rename(columns={"Unnamed: 2": "gp_indc"})

# Create filtered dataset to only include data from played games
gp_data = data.loc[data['gp_indc'] == 'boxscore']
    
# Change data types
gp_data['Gm#'] = gp_data['Gm#'].astype(int)
gp_data['R'] = gp_data['R'].astype(int)
gp_data['RA'] = gp_data['RA'].astype(int)

# %% Calculate new columns
# Create cumulative sums of runs scored and runs allowed
gp_data['cumsum_rs'] = gp_data['R'].cumsum()
gp_data['cumsum_ra'] = gp_data['RA'].cumsum()

# Calculate running estimated win percentage column
exp = 1.85
gp_data['est_wpct'] = (gp_data['cumsum_rs'] ** exp)\
                      / ((gp_data['cumsum_rs'] ** exp)\
                      + (gp_data['cumsum_ra'] ** exp))

# Calculate running estimated season wins column
gt = 162
gp_data['est_wins'] = gp_data['est_wpct'] * gt

print(gp_data['est_wins'].max(), )

# %% Check table buildout so far
print(gp_data.head())
for col in gp_data.columns:
    print(col)

# %% Plot cumulative runs scored and cumulative runs allowed across games played
plt.plot(gp_data['Gm#'], gp_data['cumsum_rs'], color='#0C2340')
plt.plot(gp_data['Gm#'], gp_data['cumsum_ra'], color='#BD3039')
plt.legend(['Runs Scored', 'Runs Allowed'])
plt.show()

# %% Plot cumulative vs scored and cumulative runs allowed across games played
rng = [*range(0, gp_data['cumsum_rs'].max(), 1)]

plt.plot(gp_data['cumsum_ra'], gp_data['cumsum_rs'], color='#0C2340')
plt.plot(rng, rng, color='black')
plt.show()

# %% Plot running estimated season wins over games played
plt.plot(gp_data['Gm#'], gp_data['est_wins'], color='#0C2340')
plt.show()
                 
# %% Plot runs scored versus runs allowed across games played
plt.scatter(gp_data['RA'], gp_data['R'], color='#0C2340')
plt.show()

# %% Calculate total runs, runs allowed, and games played YTD
#calculate runs scored and save to variable 'rs'
rs = pd.to_numeric(gp_data['R']).sum()

#calculate runs allowed and save to variable 'ra'
ra = pd.to_numeric(gp_data['RA']).sum()

gp = gp_data['gp_indc'].count()

# %% Calculate current pythagorean win expectation
exp = 1.85
gt = 162
est_wpct = (rs ** exp) / ((rs ** exp) + (ra ** exp))
est_wins = est_wpct * gt

print(est_wpct)
print("This season, the Red Sox are estimated to win " + str(round(est_wins, 0)) + " games")


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
