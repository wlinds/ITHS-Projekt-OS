from __future__ import annotations

# TODO: Info om använding och projekt etc. länkar, etc.


# Formalia:
# - Are we doing 'this' or "this"? -- rn i'm doing both... /wil
# - Should we do the layout in here or in other .py?
# - Should we have other scripts for functions or everything in main?
#
# </formalia>

# Run this with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

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

path_a, path_b = "Data/athlete_events.csv", "Data/noc_regions.csv"
external_stylesheets = 'default.css' # css used for styling, can be changed
external_scripts = [] # for javascript if we want to add

# ----- Begin functions ----- #

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


# test function for medals
def plot_test(value):
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

# Country selector, can be changed.  -- We could make this into callback function to get user input to select any 'Country' value.
df_GER = df.loc[df['Country'] == "Germany"]
df_SWE = df.loc[df['Country'] == "Sweden"]
#etc

# List of all available Countries 
country_li = df['Country'].unique().tolist()
country_li.pop(159) # Remove missing value, idk why there's a missing value, but its gone now.



#--------------------- Begin dash layout -------------------------------#









# --------------------- Ideas ---------------- #

# what if we did predictive text?
# run input value into algorithm and return predicted country from DataFrame?

# Test box
app.layout = html.Div([
    html.H2("Search country:", ),
    html.Div([dcc.Input(id='user-input', value=None)]),
    html.Br(),
    html.Div(id='my-output'),
])

@app.callback(
    Output(component_id='my-output', component_property='children'),
    Input(component_id='user-input', component_property='value'))

# Function to predict country from user input keys
# TODO: defaults to list item[0], Afghanistan, while no input is present (should: clear input) 
def regex_filter(value):
    test_list = country_li
    r = re.compile(value)
    filtered_list = list(filter(r.match, test_list))
    if len(filtered_list) != 0:
        print(f'{value=}', {filtered_list[0]})
        return filtered_list[0]
    else: return "No country found: Did you mean: 'suggested value'" # TODO

def update_output_div(input_value):
    return regex_filter(input_value)

if __name__ == '__main__':
    app.run_server(debug=True)