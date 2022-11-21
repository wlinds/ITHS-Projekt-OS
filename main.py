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
from input import OlympicData
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



# Text field, H1, left
def drawH1(Paragraph="Text"):
    return html.Div([
        dbc.Card(
            dbc.CardBody([
                html.Div([
                    html.H1(Paragraph),
                ], style={'textAlign': 'Left'}) 
            ])
        ),
    ])

# Text field, H4, Center
def drawH4(Paragraph="Text"):
    return html.Div([
        dbc.Card(
            dbc.CardBody([
                html.Div([
                    html.H4(Paragraph),
                ], style={'textAlign': 'Center'}) 
            ])
        ),
    ])


# Bar figure test
def drawFigure():
    return  html.Div([
        dbc.Card(
            dbc.CardBody([
                dcc.Graph(
                    figure=px.bar(
                        df_medal, x="Medal", y="Country", title="Medals").update_layout(),
                    config={
                        'displayModeBar': False
                    }
                ) 
            ])
        ),  
    ])

def drawFigure2():
    return  html.Div([
        dbc.Card(
            dbc.CardBody([
                dcc.Graph(
                    figure=px.bar(
                        df_medal, x="Medal", y="Country", title="Medals").update_layout(),
                    config={
                        'displayModeBar': False
                    }
                ) 
            ])
        ),  
    ])

# This function creates an input element which maps to 'user-input' and 'my-output' 
def input_box():
    return html.Div(
        dbc.Card(
            dbc.CardBody([
            html.Div([
                html.H4("Search country:", ),
            html.Div([dcc.Input(id='user-input', value=None)]),
                html.Br(),
            html.Div(id='my-output')])
    ])
    ))

def top_country_medals(my_country):
    "Loops through selected medals, drops missing values. Returns list." # not very efficient but kinda works.
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
    
    app.layout = html.Div([
        dbc.Card(
            dbc.CardBody([
                dbc.Row([
                    dbc.Col([
                        drawH1("Hi, I'm a title in H1, aligned left.")
                    ], width=3),
                    dbc.Col([
                        drawH4("I'm a paragraph in H4, centered")
                    ], width=3),

                ], align='center'), 
                html.Br(),
                dbc.Row([
                    dbc.Col([
                        drawFigure() 
                    ], width=3),
                    dbc.Col([
                        drawFigure()
                    ], width=3),
                    dbc.Col([
                        drawFigure() 
                    ], width=6),
                ], align='center'), 
                html.Br(),
                dbc.Row([
                    dbc.Col([
                        drawFigure()
                    ], width=9),
                    dbc.Col([
                        drawFigure()
                    ], width=3),
                ], align='center'),


                dbc.Row([
                    dbc.Col([
                        input_box()
                    
                    ]),
                    dbc.Col([
                        drawFigure()
                    ], width=9),
                
                


                ])
                   
            ]), color = 'dark'
        )
    ])
    app.run_server(debug=True)