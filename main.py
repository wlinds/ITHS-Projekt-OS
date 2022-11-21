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
app.title="Olympic Games"
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


df_GER2 = extract_data(path_a, path_b, ['Name', 'Age', 'NOC', 'Games', 'Year', 'Sport', 'Medal'], hash=True, country_select="Germany")

#--------------------- Begin dash layout -------------------------------#

# Only use Row and Col inside a Container. Set fluid=True to remove default container margins.
# The immediate children of any Row component should always be Col components. Content/figs should go inside the Col components.











# --- Regex search box idea --- # 
search_box = html.Div = (
    html.Div([
    html.H4("Search country:", ),
    html.Div([dcc.Input(id='user-input', value=None)]),
    html.Br(),
    html.Div(id='my-output')
    ])
    )

def top_country_medals(my_country):
    "Loops through selected medals, drops missing values. Returns list." # ot very efficient but kinda works.
    my_medal = ['Gold','Silver','Bronze']
    medal_li = []
    df_ger = extract_data(path_a, path_b, ['Name', 'NOC', 'Medal'], hash=False, country_select=my_country).dropna()
    for count, i in enumerate(my_medal, start=0):
        df1 = df_ger[df_ger.Medal == my_medal[count]]
        medal_li.append(f"{i}: {len(df1)}. ")
    medal_li.insert(0, my_country + ": ")
    return medal_li

def regex_filter(value): # Function to predict country from user input keys, TODO: defaults to list item[0], Afghanistan, while no input is present (should: clear input)
    if value == None: # Prevents error for no user input
        return None
    test_list = country_li
    r = re.compile(value)
    filtered_list = list(filter(r.match, test_list))
    if len(filtered_list) > 0:
        print(f'{value=}', {filtered_list[0]})
        return top_country_medals(filtered_list[0])
    else: return "No country found: Did you mean: 'suggested value'" # TODO

@app.callback(
      Output(component_id='my-output', component_property='children'),
      Input(component_id='user-input', component_property='value'))

def update_output_div(input_value):
    if input_value == None:
        return None
    print(input_value)
    return regex_filter(input_value)


if __name__ == '__main__':
    app.layout = search_box
    app.run_server(debug=True)