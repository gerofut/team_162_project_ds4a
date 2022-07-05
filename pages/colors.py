import dash
import pandas as pd
from dash import html , dcc, callback, Input, Output
import dash_bootstrap_components as dbc
from dash_labs.plugins import register_page
import plotly.express as px
import datetime

## Register the page in dash_labs_plugin
register_page(__name__, path="/colors")

## Define the dataframe and prepare the data for the plot
colors = pd.read_csv('/home/crnox95/ds4a_project/data/csv/colors.csv',sep=',')

## define the layout of the page
layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.Div([
                html.H1("WHAT COLORS ARE MOST SOLD IN H&M", className=" text-sm-center mb-4"),
            ]),
                    dbc.Row( #row 3 --> Date picker to select the month
            dbc.Col(
                html.Div(
                    dcc.DatePickerRange(
                        id='date-picker-range',
                        min_date_allowed=colors.t_dat.min(),
                        max_date_allowed=colors.t_dat.max(),
                        initial_visible_month=colors.t_dat.min(),
                        start_date=colors.t_dat.min(),
                        end_date=colors.t_dat.max(),
                        display_format='MMM YYYY',
                        className='dark-theme-control',
                        
                        
                    ),
                    title="Select a date range to visualize sells by colour group",
                    
                ), 
                align="center", 
                className="text-sm-center mb-4", 
                width={"size":12, "order":1},
                
            )  
        ),
        dbc.Row([  #row 4 --> Line plot
        dbc.Col(
            html.Div(
                dcc.Graph(figure={}, id='barplot-colors', style= {'backgroundColor': '#000000', 'color': '#000000', 'width': '100%'} ),className="mb-4"
                ),width= 12,
            ),
        ]),
        ])
    ])
])

#############################################################################################################################
# CALLBACKS
#############################################################################################################################
@callback(
    Output(component_id='barplot-colors', component_property='figure'),
    [Input(component_id='date-picker-range', component_property='start_date'),
     Input(component_id='date-picker-range', component_property='end_date')],
)

def update_barplot(start_date, end_date):
    colors_filt = colors[(colors.t_dat >= start_date) & (colors.t_dat <= end_date)]
    colors_group = colors_filt.groupby(['color'])['color'].count().sort_values(ascending = False).head(10)
    df_agg = pd.DataFrame(colors_group)
    ### Figure: bar plot
    fig = px.bar(df_agg, x = df_agg.index, y = 'color',
                    labels={
                     "color": "Amount sold",
                     "index": "Color of items"
                 } )
    fig.update_layout(title= f"Top ten color hues sold in H&M from {start_date[:-3]} to {end_date[:-3]}",
                 title_x=0.5)
    return fig