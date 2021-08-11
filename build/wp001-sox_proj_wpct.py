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

# %% 2. Import data
data = pd.read_csv(r'/Users/YouCanCallMeAll/Desktop/Baseball/wp001-sox_proj_wpct/data/sox_game_results.csv')
print(data.head())
for col in data.columns:
    print(col)

# %% Cleanse data
    
#rename columns
data.rename(columns={"Unnamed: 2": "gp_indc"})
    
# %% Calculate total runs, runs allowed, and games played YTD

#filter for only data from games played
gp_data = data[data['gp_indc'] == 'boxscore']
#print(gp_data)

#calculate runs scored and save to variable 'rs'
rs = pd.to_numeric(gp_data['R']).sum()
#print(rs)

#calculate runs allowed and save to variable 'ra'
ra = pd.to_numeric(gp_data['RA']).sum()
#print(ra)

gp = gp_data['gp_indc'].count()
#print(gp)

# %% Create cumulative sums of runs scored and runs allowed

# %% Plot runs scored and runs allowed across games played

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
