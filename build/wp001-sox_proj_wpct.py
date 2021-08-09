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
    
# %% 3. Calculate total runs, runs allowed, and games played YTD
