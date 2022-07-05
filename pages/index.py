import pandas as pd
import plotly.express as px 
pie=pd.read_csv('/home/crnox95/ds4a_project/data/csv/piechart.csv')
import dash
import dash_bootstrap_components as dbc
from dash import Dash, dcc, html, Input, Output, callback
from IPython.display import HTML
from dash_labs.plugins import register_page

register_page(__name__, path="/Index")


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
        {"label":"enero","value":1},
        {"label":"febrero","value":2},
        {"label":"marzo","value":3},
        {"label":"abril","value":4},
        {"label":"mayo","value":5},
        {"label":"junio","value":6},
        {"label":"julio","value":7},
        {"label":"agosto","value":8},
        {"label":"septiembre","value":9},
        {"label":"octubre","value":10},
        {"label":"noviembre","value":11},
        {"label":"diciembre","value":12},
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
