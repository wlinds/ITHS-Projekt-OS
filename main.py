
import os
import pandas as pd
from input import * 
import dash
from dash import html
from dash import dcc
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objects as go
from dash.dependencies import Input, Output


# initialize app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.UNITED]) # bootstrap theme

# graph 1 is for age distribution
fig1 = px.histogram(df_germany, x='Age', color = 'Sex',  title= "Histogram of ages")


# graph 2 for total number if womens from Germany participated in olympics
df_female= df_germany[['Year','Sex',"Season"]]
df_female = df_female[(df_female['Sex'] == 'F')]
# separte data frame created
females= df_female[['Year','Season']].value_counts().reset_index(name = 'count').sort_values(by ="Year", ascending= True)

fig2 = px.line(females, x = "Year" , y="count", color= "Season", log_x = True, title = " Total number of females participated in Olympics")


# graph 3 represents top 10 sports germany got medals
df_medals = pd.DataFrame(df_germany.groupby("Sport")["Medal"].count().sort_values(ascending= False)).reset_index().head(10)
fig3 = fig = px.bar(df_medals,x="Sport",
    y="Medal",color = "Sport",
    labels={"Sport": "Sport", "value": "Number of medals"}, title= "Top 10 sports in Germany won the most medals")

# set up layout
app.layout = html.Div(children=[
    # All elements from the top of the page
    html.Div([
        html.Div([
            html.H1(children='Land Statstics: GERMANY'),
            
            dcc.Dropdown(
                options=[{'label': "Year", 'value': "Year"},{'label': "Weight", 'value': "Weight"}, 
                {'label': "Height", 'value': "Height"}, {'label': "Age", 'value': "Age"}, {'label': "Season", 'value': "Season"}],
                value='Age',
                id='dropdown1'
            ),

            dcc.Graph(
                id='histogram',
                figure=fig1
            ),

        ], className='six columns'),
        html.Div([
            html.H1(children=''),

            html.Div(children='''
                Dash: Grapically represents women empowerment.
            '''),
            dcc.Dropdown(
                options=[{'label': i, 'value': i} for i in df_germany.columns],
                value='Sex',
                id='dropdown2',
                style={"width": "50%", "offset":1,},
                clearable=False,
            ),

            dcc.Graph(
                id='scatter',
                figure=fig2
            ),  
        ], className='six columns'),
    ], className='row'),
    # New Div for all elements in the new 'row' of the page
    html.Div([
        html.H1(children='Hello Dash'),

        html.Div(children='''
            Dash: Top medal analysis.
        '''),
        dcc.Dropdown(
                options=[{'label': i, 'value': i} for i in df_germany.columns],
                value='Medal',
                id='dropdown',
                style={"width": "50%", "offset":1,},
                clearable=False,
            ),

        dcc.Graph(
            id='bar',
            figure=fig3
        ),  
    ], className='row'),
])

# callbacks
@app.callback(
    Output(component_id='histogram', component_property='figure'),
    Output(component_id='line', component_property='figure'),
    Output(component_id='histogram', component_property='figure'),

    Input(component_id='dropdown1', component_property='value'),
    Input(component_id='dropdown2', component_property='value'),
    Input(component_id='dropdown', component_property='value'),
)

def update_hist(feature):
    fig1 = px.histogram(df_germany, x=feature)
    return fig1

def update_output(value):
    return f'You have selected {value}'




if __name__ == '__main__':
    app.run_server(debug=True)

    
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
