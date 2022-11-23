from __future__ import annotations
import os
import pandas as pd
from input import df_germany, df_merge, all_region
import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
import plotly.express as px
from dash.dependencies import Input, Output
import plotly.graph_objects as go
import re
from graph import *


from graph import total_individual_xcs_plot
from graph import women_team_xcs_plot
from graph import men_team_xcs_plot
from graph import germany_xcs

# TODO: Info om använding och projekt etc. länkar, etc.
# This app analyzes data from the olympic games.
# Run this and visit http://127.0.0.1:8050/ in your web browser.

# initialize app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.UNITED]) # bootstrap theme


server = app.server
# ----- Figure functions followed by return function ----- #

def no_bg(fig: px.Figure) -> px.Figure:
    "Removes backfround from fig"
    return fig.update_layout(plot_bgcolor = 'rgba(0, 0, 0, 0)')



# -> Renders age_gender_histogram in layout
def dash_plot1():
    return html.Div([
            dcc.Graph(
                id='histogram',
                figure=no_bg(age_gender_historgram())
            ),
        ])



# -> Renders medal_graph in layout
def top_medal():
     return html.Div([
        dcc.Graph(
            id='top_medal_bar',
            figure=medal_graph(),)
            ])



# -> Renders season_participation in layout
def seasonal_pie():
    return html.Div([
            dcc.Graph(
                id='season-pie',
                figure=season_participation()
            ),
        ])


# -> Renders females participated by country
def female_part():
    return html.Div([
            dcc.Graph(


                id='female-part',
                figure=female_participation()
            ),
        ])



# Cross country skiing functions. used to plot xcs._____________________________
# required to plot men_team_xcs_plot
def xcs_men():
    return html.Div(
        [
            dcc.Graph(id="xcs-men-test", figure=men_team_xcs_plot())
        ]
    )

def xcs_women():
    return html.Div(
        [
            dcc.Graph(id="xcs-women", figure=women_team_xcs_plot())
        ]
    )

def xcs_individual():
    return html.Div(
        [
            dcc.Graph(id="xcs-individual", figure=total_individual_xcs_plot())
        ]
    )

def xcs_germany_plot():
    return html.Div(
        [
            dcc.Graph(id="xcs-germany-plot", figure=germany_xcs())
        ]
    )
#________________________________________________________________


    
# -> Renders top sports participated by country
def sport_part():
    return html.Div([
            dcc.Graph(


                id='sport-part',
                figure=sport_participation()
            ),
        ])

# ----- Divs & dbc.Cards & other componentes ----- #

# Just a header row - top menu with 100% width.
def header(title,region,flag):
    return html.Div([
        html.Div(
            className="olympic-header",
            children=[
            dbc.Row(
                [dbc.Col(html.H1(title + ": " + (region + " " + flag)))]
                )
    ])
])

# Box for presenting text - Used for titles and subtitles. 
def info_box(title=None, paragraph=None, css_class=None):
    return html.Div(className=css_class,
    children=[
        dbc.Row([
        html.H2(title),

        html.P(paragraph)],
        justify="center", align="center", className="h-50")]
    )

def search_country(css_class=None):
    return html.Div([
            html.H6("Enter any country:"),

            dbc.Col(dcc.Input(id='search-box-user-input', value=None)),

            html.Div(id='country-select-output')], className=css_class)


# First box - contains country specific graphs
def div1():
    return html.Div([
        dbc.Row(
            [
                dbc.Col(html.Div(dash_plot1()), md=6),
                dbc.Col(html.Div(top_medal()), md=6),
            ]
        ),
        dbc.Row(
            [
                dbc.Col(html.Div(seasonal_pie()), md=6),
                dbc.Col(html.Div(female_part()), md=6),
            ])

            ], style={'marginRight': 15, 'marginLeft': 15, 'marginBottom': 50, 'marginTop': 25}
    )



    


 # contains sports graphs
def div2():
     return dbc.Card([
            html.H1(),

            html.Div(),


        dbc.Row(
            [
                dbc.Col(html.Div(xcs_women()), md=6),
                dbc.Col(html.Div(xcs_men()), md=6)

            ]
        ),
        dbc.Row(
            [
                dbc.Col(html.Div(xcs_individual()), md=6),
                 dbc.Col(html.Div(sport_part()), md=6)
            ]
        )
        ])


         
       


    # New Div for all elements in the new 'row' of the page
   
def div3():
    return dbc.Card([
        html.H1(children='Hello Dash'),
        

        html.Div(children='''
            Dash: Top medal analysis.
        '''),
        dcc.Dropdown(
                options=[{'label': i, 'value': i} for i in df_germany.columns],
                value='Medal',
                id='xcs-germany-plot',
                style={"width": "50%", "offset":1,},
                clearable=False,
            ),
                    dbc.Row(
            [
                dbc.Col(html.Div(xcs_germany_plot()), md=10)
            ]
        )
    ])



def about_box():
    return html.Div(
    dcc.Markdown('''
## About
This tool should be used for estimates only. Data integrity not guaranteed. Use at own risk. 
- Placeholder text.

    '''),
    
    style={'marginRight': 15, 'marginLeft': 15, 'marginBottom': 50, 'marginTop': 25})

def footer(value="Default value: Hellö."):
    return dbc.Card(
    [
        dbc.CardBody([
            html.H6(value, className="footer"),
            ]),
    ],
    style={"width": '100%'},
)

@app.callback(
      Output(component_id='country-select-output', component_property='children'),
      #Output(component_id='xcs-germany-plot', component_property='children'),
      Input(component_id='search-box-user-input', component_property='value'),)
     # Input(component_id='xcs-germany-plot', component_property='value'))

def update_output_div(input_value):
    if input_value == None:
        return None
    print(input_value)
    return regex_filter(input_value)

# ----- Functions & data ----- #

def regex_filter(value): # Function to predict country from user input keys
    if value == None: # Prevents error for no user input
        return None
    test_list = all_region
    r = re.compile(value)
    filtered_list = list(filter(r.match, test_list))
    if len(filtered_list) > 0:
        print(f'{value=}', {filtered_list[0]})
        return filtered_list[0]
    else: return "No country found: Did you mean: 'suggested value'" # TODO

def flag_algo(selected_region):
    # Pretty sure there's a way to map this, this works for now but only works for Swe & Ger
    if selected_region == "Germany":
        return ("\U0001F1E9" + "\U0001F1EA")
    elif selected_region == "Sweden":
        return("\U0001F1F8" + "\U0001F1EA")
    else: return ("\U0001F3AF") # Placeholder emoji

if __name__ == '__main__':

    select_region = "Germany" # Region selector, defaults to Germany
    compare_region = "Sweden" # Variable used to compare with region

    # Get any region df - Can we implement this in input.py? /wil
    def get_region(df, region):
        return df.loc[df['region'] == region]

    active_region1 = get_region(df_merge, select_region)
    active_region2 = get_region(df_merge, compare_region)

    # Emoji flag, inherits defalut from selected_region
    flag = flag_algo(select_region)

    # This could also be a variable, I'm thinking webscraping google and returning first search result for ([country]+"slogan") as string.
    country_slogan = "Unity and justice and freedom."
    

    # Main building blocks for frontend. 
    app.layout = html.Div([

        # Just the header. Curretly weird search box. Will fix.
        header("Olymic Games Data", select_region, flag),

        #Info_box with title, never changes.
        info_box("Olympic Games. Visualised through trial and error.","A brief history of the Olympic Games through collaborative data analysis.", "olympic-act1"),

        # search box
        search_country("region-search-box"),

        #Info about selected country, defaults to Germany
        info_box((select_region + flag), country_slogan, "olympic-act2"),
        div1(),

        # Info about all countries
        info_box((("All countries " + "\U0001F30E")),"Sport specific", "olympic-act1"),
        div2(),div3(),

        # About us and the project, idk?
        about_box(),

        # Just a footer with ITHS
        footer('ITHS AI22 | Databehandling - Grupp Tyskland'),
        ])

    app.run_server(debug=True)