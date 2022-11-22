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



# initialize app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.UNITED])
# set app layout
app.layout = html.Div(children=[
    html.H1('Test Dash App', style={'textAlign':'center'}),
    html.Br(),
    dcc.Dropdown(
        options=[{'label': i, 'value': i} for i in df_germany.columns],
        value='Age',
        id='dropdown',
        style={"width": "50%", "offset":1,},
        clearable=False,
    ),
    dcc.Graph(id='histogram')
])
# callbacks
@app.callback(
    Output(component_id='histogram', component_property='figure'),
    Input(component_id='dropdown', component_property='value'),
)
def update_hist(feature):
    fig = px.histogram(df, x=feature)
    return fig
if __name__ == "__main__":
    app.run_server(debug=True)