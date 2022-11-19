from __future__ import annotations

# TODO: Info om använding och projekt etc. länkar, etc.

# This app analyzes data from the olympic games.
# Run this and visit http://127.0.0.1:8050/ in your web browser.

import pandas as pd
import numpy as np
import dash
import os
from dash import callback, html, Input, Output, dash_table, dcc
import dash_bootstrap_components as dbc
import plotly_express as px
from input import extract_data
import re

app = dash.Dash(__name__)
app.title="Untitled"
external_stylesheets = 'default.css'

path_a, path_b = "Data/athlete_events.csv", "Data/noc_regions.csv"
usecols = ['Name', 'Age', 'Sex', 'Team', 'NOC', 'Games', 'Year', 'Sport', 'Medal'] # cols to be selected when reading path_a

# Example: df with all countries
df_all = extract_data(path_a, path_b, usecols, hash=True, country_select="All")

# Example: this creates df with Germany
df_GER = extract_data(path_a, path_b, usecols, hash=True, country_select="Germany")

# Example: List of all available Countries 
country_li = df_all['Country'].unique().tolist()
country_li.pop(159) # Remove missing value, idk why there's a missing value, but its gone now.

# This creates df with all medals #TODO: Separate team medals from country medals
df_medal = df_all.groupby("Country")[["Medal"]].count().sort_values(by = "Medal",ascending= False).head(10).reset_index()
print(df_medal.head)

#--------------------- Begin dash layout -------------------------------#




if __name__ == '__main__':
    app.run_server(debug=True)