# Typ TODO: Info om använding och projekt etc. länkar, etc.

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

app = dash.Dash(__name__)
external_stylesheet = 'default.css' # css used for styling
df = pd.read_csv("Data/athlete_events.csv", usecols=['Name', 'Age', 'Sex', 'Team', 'NOC','Games','Year','Sport','Medal'])
df1 = pd.read_csv("Data/noc_regions.csv",usecols=['region', 'NOC']) #### NOC: National Olympic Committee

#---------------------------------------------------------#

# replace column Name with all hashed names (not germany only)
df1["Name"] = hash_names(df, "Name")

# merge both files with corresconding columns - why are we doing this? /will
df_merge = df1.merge(df, on="NOC",how = "left")


## This does nothing at the moment - just leftover from trying buttons and forms
## We will need the callback and layout structures for the app later

# https://dash.plotly.com/basic-callbacks

app.layout = html.Div([
    html.H6("Change the value in the text box to see callbacks in action!"),
    html.Div([
        "Input: ",
        dcc.Input(id='my-input', value='initial value', type='text')
    ]),
    html.Br(),
    html.Div(id='my-output'),

])


@app.callback(
    Output(component_id='my-output', component_property='children'),
    Input(component_id='my-input', component_property='value')
)
def update_output_div(input_value):
    return f'Output: {input_value}'

def callback(n_clicks):
    return [f"Called {n_clicks} times"]

if __name__ == '__main__':
    app.run_server(debug=True)