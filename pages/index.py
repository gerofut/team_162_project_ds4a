from dash import html , dcc, callback, Input, Output
import dash_bootstrap_components as dbc
from dash_labs.plugins import register_page
import plotly.express as px

register_page(__name__, path="/Index")


layout = dbc.Container(
    dbc.Row(
        dbc.Col([
            dcc.Dropdown(['2018', '2019','2020'], '', id='demo-dropdown'),
            html.Div([
                dcc.Graph(figure={},id="graficapie")
            ],id="graficapie"),  
        ])
    )
)


@callback(
    Output(component_id='graficapie',component_property="figure"),
    Input(component_id='demo-dropdown',component_property='value')
)
def update_output(value):
    fig = px.pie(x,values=x["cantidad"],names=x["index_group_name"],title='Population of European continent')
    fig.update_traces( textfont_size=10,marker=dict(line=dict(color='black', width=1.5)))
    return fig

