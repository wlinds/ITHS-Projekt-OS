from __future__ import annotations

# TODO: Info om använding och projekt etc. länkar, etc.

# Run this and visit http://127.0.0.1:8050/ in your web browser.

import pandas as pd
import numpy as np
import dash
import os
from dash import callback, html, Input, Output, dash_table, dcc
import dash_bootstrap_components as dbc
import plotly_express as px
from hash import hash_names
import re

app = dash.Dash(__name__)
app.title="Untitled"

path_a, path_b = "Data/athlete_events.csv", "Data/noc_regions.csv" # import, can be moved to input.py
external_stylesheets = 'default.css' # css used for styling, can be changed
external_scripts = [] # for javascript if we want to add

# ----- Begin functions ----- #

# TODO: Move to input.py
def extract_data(path_a, path_b): 
    """Takes two csv files, calls hash.py, merges and returns DataFrame.""" #TODO: Create nice parameters (What to hash, which columns to use etc.)

    df = pd.read_csv(path_a,
        usecols=['Name', 'Age', 'Sex', 'Team', 'NOC', 'Games', 'Year', 'Sport', 'Medal'])  # Could be selected with callback as parameters but it might be slow (?)
    df1 = pd.read_csv(path_b,
        usecols=['region', 'NOC'])

    # Calling hash.py, hashing names
    df["Name"] = hash_names(df, "Name")

    # Left outer join merge, -> how to explain this (?) why isn't NOC already formatted in df
    return df1.merge(df, on="NOC", how = "left")


    """Test plotting function."""
    fig = px.bar(value, x="Country",
    y=0,color ="Medal",
    log_y = True,
    labels={"value": "value", "0": "Number of medals"}, title= value)
    return fig


# ----- Begin main ----- #

# Call function to create anonymized athlete name column in DataFrame and merge two input csv for all countries
df = extract_data(path_a,path_b)

# Change title 'region' to 'Country' (should we put this in extract_data function? /wil)
df.rename(columns = {'region':'Country'}, inplace=True)

# Country selector, can be changed.
df_GER = df.loc[df['Country'] == "Germany"]

# List of all available Countries 
country_li = df['Country'].unique().tolist()
country_li.pop(159) # Remove missing value, idk why there's a missing value, but its gone now.

#--------------------- Begin dash layout -------------------------------#









if __name__ == '__main__':
    app.run_server(debug=True)