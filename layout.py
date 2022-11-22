from dash import html, dcc
import dash_bootstrap_components as dbc
from graph import *

def div1():
    return html.Div(
    [
        dbc.Row(
            [
                dbc.Col(html.Div(dash_plot1()), md=6),
                dbc.Col(html.Div(top_medal()), md=6),
            ]
        ),
        dbc.Row(
            [
                dbc.Col(html.Div(seasonal_pie()), md=6),
                dbc.Col(html.Div(sport_part()), md=6),
            ]
        ),

    ], style={'marginRight': 15, 'marginLeft': 15, 'marginBottom': 50, 'marginTop': 25})



def div2():
     return dbc.Card([
            html.H1('This is div2'),

            html.Div('Grapically represents women empowerment.'),

            dcc.Dropdown(
                options=[{'label': i, 'value': i} for i in df_germany.columns],
                value='Sex',
                id='dropdown2',
                style={"width": "50%", "offset":1,},
                clearable=False,
            ),
        ])

def div3():
    return dbc.Card([
        html.H1(children='Hello Dash'),

        html.Div(children='''
            Dash: Top medal analysis.
        '''),
        dcc.Dropdown(
                options=[{'label': i, 'value': i} for i in df_germany.columns],
                value='Medal',
                id='dropdown3',
                style={"width": "50%", "offset":1,},
                clearable=False,
            ),
    ])
