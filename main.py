# Typ TODO: Info om använding och projekt etc. länkar, etc.

# Run this with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import pandas as pd
import numpy as np
import dash
import os
from dash import callback, html, Input, Output, dash_table
import dash_bootstrap_components as dbc
import plotly_express as px
from hash import hash_names

app = dash.Dash(__name__)
external_stylesheet = 'default.css' # css used for styling
df = pd.read_csv("Data/athlete_events.csv", usecols=['Name', 'Age', 'Sex', 'Team', 'NOC','Games','Year','Sport','Medal'])
df1 = pd.read_csv("Data/noc_regions.csv",usecols=['region', 'NOC']) #### NOC: National Olympic Committee

#---------------------------------------------------------#

# replace column Name with all hashed names (not germany only)
df1["Name"] = hash_names(df, "Name")

# merge both files with corresconding columns
df_merge = df1.merge(df, on="NOC",how = "left")

df_germany = df_merge[df_merge["region"] == "Germany"]

medals =pd.pivot_table(
    df_germany,
    values="Year",
    index="Sport",
    columns="Medal",
    aggfunc="count",
    
    margins=True,
    
    margins_name="Total",).fillna(0).sort_values(by = "Total", ascending= False).iloc[1: , :].head(10) 

print(medals)



## This does nothing at the moment - just leftover from trying buttons and forms
## We eill need the callback and layout structures for the app later

# https://dash.plotly.com/basic-callbacks
@app.callback(
    output=Output("paragraph_id", "children"),
    inputs=Input("button_id", "n_clicks"),
)

def callback(n_clicks):
    return [f"Called {n_clicks} times"]

if __name__ == '__main__':
    app.run_server(debug=True)