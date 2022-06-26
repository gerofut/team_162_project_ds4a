import dash
import pandas as pd
from dash import html , dcc
import dash_bootstrap_components as dbc
from dash_labs.plugins import register_page
import plotly.express as px


register_page(__name__, path="/")

df = pd.read_csv('/home/crnox95/ds4a_project/data/csv/line_plot.csv')
df['year_month']=pd.to_datetime(df['year_month']).dt.to_period('M')
df.rename(columns={'year_month.1':'count'}, inplace=True)
df.set_index('year_month', inplace=True)
fig = px.line(df, x=df.index.to_timestamp(), y="count", title='H & M Sales by Month')


layout = dbc.Container(     
    [
        dbc.Row(    #row 1
            dbc.Col(
                [ #col 1
                html.H1("DATA SCIENCE FOR ALL", className="display-4"),
                html.Div(
                    [
                        html.H4('PROJECT GROUP 162', className="lead"),
                        html.Div([
                            dcc.Graph(figure=fig)
                        ])

                    ],
                    ),
                ],
            ),
                align="center",
        ),
    ],id='home-page',
)
