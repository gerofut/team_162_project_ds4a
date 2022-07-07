import pandas as pd
import plotly.express as px 
import dash
import dash_bootstrap_components as dbc
from dash import Dash, dcc, html, Input, Output, callback
from IPython.display import HTML
from dash_labs.plugins import register_page
import pathlib

## funcion to build a relative path
def get_pandas_data(csv_filename: str) -> pd.DataFrame:
   '''
   Load data from /data directory as a pandas DataFrame
   using relative paths. Relative paths are necessary for
   data loading to work in Heroku.
   '''
   PATH = pathlib.Path(__file__).parent
   DATA_PATH = PATH.joinpath("../data/csv").resolve()
   return pd.read_csv(DATA_PATH.joinpath(csv_filename))


## Register the page in dash_labs_plugin
register_page(__name__, path="/Index")

## Define the dataframe and prepare the data for the plot
pie=get_pandas_data('piechart.csv')

layout = dbc.Container([
    html.Div([
        html.H1("WHICH CATEGORIES ARE MOST SOLD IN H&M", className=" text-sm-center mb-4"),
    ]),
    html.Div([
    dcc.Dropdown([
        {"label":"2018","value":2018},
        {"label":"2019","value":2019},
        {"label":"2020","value":2020},
        ],2018,placeholder="Select a year", id='dropdownaño'),
    dcc.Dropdown([
        {"label":"January","value":1},
        {"label":"February","value":2},
        {"label":"March","value":3},
        {"label":"April","value":4},
        {"label":"May","value":5},
        {"label":"June","value":6},
        {"label":"July","value":7},
        {"label":"August","value":8},
        {"label":"September","value":9},
        {"label":"October","value":10},
        {"label":"November","value":11},
        {"label":"December","value":12},
        ],9,placeholder="Select a month", id='dropdownmes'),
    html.Div(id='dd-output-container'),
    dcc.Graph(figure={},id="graficapie")
])
])
@callback(
    Output(component_id='graficapie',component_property="figure"),
    Input(component_id='dropdownaño',component_property='value'),
    Input(component_id='dropdownmes',component_property='value')
)
def update_output(dropdownaño,dropdownmes):
    fig = px.pie(pie,values=pie[(pie['año']==dropdownaño) & (pie['mes']==dropdownmes)]["cantidad"],names=pie[(pie['año']==dropdownaño) & (pie['mes']==dropdownmes)]["index_group_name"],title='Sales for index group name by year and month') 
    fig.update_traces( textfont_size=10,marker=dict(line=dict(color='black', width=1.5)))
    return fig
