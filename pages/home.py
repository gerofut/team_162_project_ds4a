from doctest import OutputChecker
from turtle import color, width
import dash
import pandas as pd
from dash import html , dcc, callback, Input, Output
import dash_bootstrap_components as dbc
from dash_labs.plugins import register_page
import plotly.express as px
import seaborn as sns
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

register_page(__name__, path="/")

## Define the dataframe and prepare the data for the plot

## Figure 1: line-plot
df = get_pandas_data('line_plot.csv')
df['year_month']=pd.to_datetime(df['year_month']).dt.to_period('M')
df.rename(columns={'year_month.1':'count'}, inplace=True)
df.set_index('year_month', inplace=True)

## Figure 2: pie-plot
df1 = get_pandas_data('pie_plot_home.csv')
df1['year_month'] = pd.to_datetime(df1['year_month']).dt.to_period('M')
df1.set_index('year_month', inplace=True)
df1['sales_channel_id'].replace({1: 'Digital channel', 2: 'Physical channel'},inplace=True)

## Card2: amount of money
df2 = get_pandas_data('card2.csv')
df2.set_index('year_month', inplace=True)

## Define the layout of the page

layout = dbc.Container(     
    [
        dbc.Row(    #row 1 --> Title
            dbc.Col(
                [ #col 1
                html.H1("DATA SCIENCE FOR ALL COLOMBIA", className=" text-sm-center"),
                
                ],width= {"size":12, "order":1},
            ),
        ),
        dbc.Row(    #row 2 --> Subtitle
            dbc.Col([
                html.Div(
                    [
                        html.H2('PROJECT TEAM 162', className="text-sm-center"),
                        

                    ],
                    ),
                ],
            ),
            align="center",
        ),
        dbc.Row( #row 3 --> Date picker to select the month
            dbc.Col(
                html.Div(
                    dcc.DatePickerRange(
                        id='date-picker-range',
                        min_date_allowed=df.index.to_timestamp().min(),
                        max_date_allowed=df.index.to_timestamp().max(),
                        initial_visible_month=df.index.to_timestamp().min(),
                        start_date=df.index.to_timestamp().min(),
                        end_date=df.index.to_timestamp().max(),
                        display_format='MMM YYYY',
                        className='dark-theme-control',
                        
                        
                    ),
                    title="Select a date range to see the sales by month",
                    
                ), 
                align="center", 
                className="text-sm-center mb-4", 
                width={"size":12, "order":1},
                
                

            )  
        ),
        dbc.Row([  #row 4 --> Line plot
        dbc.Col(
            html.Div(
                dcc.Graph(figure={}, id='line-plot', style= {'backgroundColor': '#000000', 'color': '#000000', 'width': '100%'} ),className="mb-4"
                ),width= 6,
            ),
        dbc.Col(
            html.Div(
                dcc.Graph(figure={}, id='pie-plot')
                ),width={"size":6, "order":1},
            ),
        ]),
        dbc.Row([    #row 5 --> second line of graph and cards

        dbc.Col([
                dbc.Card([
                    dbc.CardHeader("Total Sales", className='text-sm-center'),
                    dbc.CardBody([
                         html.H2("Sales quantity", className="card-title text-sm-center"),
                            html.P("This is some card text", className="display-4 text-sm-center",id="card_text1")
                    ]),
                ], className="card text-dark  mb-3 text-sm-center",id='card1', inverse=True, 
                ),
            ]),
        dbc.Col([   
                dbc.Card([
                    dbc.CardHeader("Total Sales", className='text-sm-center'),
                    dbc.CardBody([
                         html.H2("Amount of money", className=" card-title text-sm-center"),
                            html.P("Amount of money", className="display-4 text-sm-center",id="card_text2")
                    ]),
                ], className="card text-dark  mb-3 text-sm-center",id='card2', inverse=True
            ),
        ],width={"size":6, "order":1}),

        ]),          
    ],id='home-page',
    fluid=True,
)

#############################################################################################################################
# CALLBACKS
#############################################################################################################################
@callback(
    Output(component_id='line-plot', component_property='figure'),
    Output(component_id='pie-plot', component_property='figure'),
    Output(component_id='card_text1', component_property='children'),
    Output(component_id='card_text2', component_property='children'),
    [Input(component_id='date-picker-range', component_property='start_date'),
     Input(component_id='date-picker-range', component_property='end_date')],
)

def update_line_plot(start_date, end_date):
    df_filtered = df[(df.index >= start_date) & (df.index <= end_date)]
    df1_filtered = df1[(df1.index >= start_date) & (df1.index <= end_date)]
    df2_filtered = df2[(df2.index >= start_date) & (df2.index <= end_date)]
    ### Figure 1: line-plot
    fig = px.line(df_filtered, x=df_filtered.index.to_timestamp(), y="count", title='H & M Sales by Month')
    fig.update_layout(title_text='H & M Sales over the time', title_x=0.5, xaxis_title='Date', yaxis_title='Sales')
    ### Figure 2: pie-plot
    fig2 = px.pie(df1_filtered.reset_index(),values='count',names='sales_channel_id', title='Sales by Channel', hole=.3 )
    fig2.update_layout(title_text='Sales by channel', title_x=0.5, legend_title='Sales Channel' )


    card1 = '{:,}'.format(df_filtered['count'].sum())
    card2 = '${:,}'.format(df2_filtered['price'].sum().round(0))
    
    return fig, fig2, card1, card2