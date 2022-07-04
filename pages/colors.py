import dash
import pandas as pd
from dash import html 
import dash_bootstrap_components as dbc
from dash_labs.plugins import register_page

## Register the page in dash_labs_plugin
register_page(__name__, path="/colors")

## Define the dataframe and prepare the data for the plot

## define the layout of the page
layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.Div([
                html.H1("WHAT COLORS ARE MOST SOLD IN H&M", className=" text-sm-center mb-4"),
            ])
        ])
    ])
])