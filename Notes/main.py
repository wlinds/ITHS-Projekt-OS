import os
from load_data import OlympicData
import pandas as pd
import dash
from dash import html
from dash import dcc
import dash_bootstrap_components as dbc
import plotly.express as px
from dash.dependencies import Input, Output

directory_path = os.path.dirname(__file__)
path = os.path.join(directory_path, "olympicdata")

print(path)

olympicdata_object = OlympicData(path)
 
 # load data
df = olympicdata_object.olympic_dataframe("athlete_events")
df1 = olympicdata_object.olympic_dataframe("noc_regions")

# merge both the files with corresconding columns
df_merge = pd.merge(df, df1,  on="NOC",how = "left")
#print(df_merge)

# select only data of our group : germany
df_germany = df_merge[(df_merge["region"] == "Germany")]


# make plot
fig1 = px.histogram(df_germany, x='Age', color = 'Sex',  title= "Histogram of ages")
fig2 = px.bar(df_germany, x="Sport", y = "Medal")

# initialize app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.UNITED]) # bootstrap theme


# set up layout
app.layout = html.Div(children=[
    # All elements from the top of the page
    html.Div([
        html.H1(children='Land Statstics : GERMANY'),

        html.Div(children='''
            Dash: Grapically represents land statstics.
        '''),

        dcc.Graph(
            id='histogram',
            figure=fig1
        ),  
    ]),
    # New Div for all elements in the new 'row' of the page
    html.Div([ 
        dcc.Dropdown(
        options=[{'label': i, 'value': i} for i in df_germany.columns],
        value='Medal',
        id='dropdown',
        style={"width": "50%", "offset":1,},
        clearable=False,
    ),
    dcc.Graph(id='bar', figure=fig2)
])
])

# callbacks
@app.callback(
    Output(component_id='histogram', component_property='figure'),
    Output(component_id='bar', component_property='figure'),
    Input(component_id='dropdown', component_property='value'),
)

def update_hist(feature):
    fig1 = px.histogram(df_germany, x=feature)
    return fig1


# to run app
if __name__ == "__main__":
    app.run_server(debug=True)


