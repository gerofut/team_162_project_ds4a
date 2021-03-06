import dash
import pandas as pd
from dash import html , dcc, callback, Input, Output
import dash_bootstrap_components as dbc
from dash_labs.plugins import register_page
import numpy as np
import pandas as pd
import pickle
import sklearn
import plotly.express as px
import base64
import pathlib

## funcion to build a relative path
def get_pickle_data(pickle_model: str):
   '''
   Load data from /data directory as a pandas DataFrame
   using relative paths. Relative paths are necessary for
   data loading to work in Heroku.
   '''
   PATH = pathlib.Path(__file__).parent
   DATA_PATH = PATH.joinpath("../data/models").resolve()
   return pickle.load(open(DATA_PATH.joinpath(pickle_model), 'rb'))

## Register the page in dash_labs_plugin

register_page(__name__, path="/prediction")

# ##  Load images
# ##  digital sales images
# image_filename = '/home/crnox95/ds4a_project/data/images/digital_sales.png'
# encoded_image = base64.b64encode(open(image_filename, 'rb').read())

##  function for convert text to number with decimals
def text_to_number(text):
    return float(text.replace(',','.'))

## list of encoders to be used in the prediction function

encoder_garments ={'Under-, Nightwear':1, 'Blouses':2, 'Knitwear':3, 'Special Offers':4,
    'Shoes':5, 'Accessories':6, 'Skirts':7, 'Trousers':8, 'Dresses Ladies':9,
    'Jersey Basic':10, 'Jersey Fancy':11, 'Socks and Tights':12, 'Swimwear':13,
    'Trousers Denim':14, 'Unknown':15, 'Woven/Jersey/Knitted mix Baby':16,
    'Outdoor':17, 'Shirts':18, 'Dressed':19, 'Dresses/Skirts girls':20, 'Shorts':21}
    
encoder_colors ={'Black':1, 'Light Pink':2, 'Light Blue':3, 'Pink':4, 'Dark Green':5,
    'Dark Grey':6, 'Grey':7, 'Dark Blue':8, 'Dark Pink':9, 'Light Red':10,
    'Beige':11, 'Dark Yellow':12, 'Green':13, 'Gold':14, 'White':15, 'Light Grey':16,
    'Red':17, 'Orange':18, 'Light Orange':19, 'Dark Turquoise':20, 'Other':21,
    'Yellowish Brown':22, 'Dark Red':23, 'Light Beige':24, 'Yellow':25,
    'Turquoise':26, 'Blue':27, 'Other Pink':28, 'Dark Beige':29, 'Greenish Khaki':30,
    'Off White':31, 'Light Green':32, 'Silver':33, 'Light Yellow':34,
    'Light Purple':35, 'Dark Purple':36, 'Purple':37, 'Greyish Beige':38,
    'Light Turquoise':39, 'Other Blue':40, 'Dark Orange':41, 'Other Turquoise':42,
    'Bronze/Copper':43, 'Other Red':44, 'Transparent':45, 'Other Yellow':46,
    'Other Orange':47, 'Other Purple':48, 'Unknown':49, 'Other Green':50}
    
encoder_index_groups = {'Ladieswear':1, 'Divided':2, 'Menswear':3, 'Sport':4, 'Baby/Children':5}


## Define the layout of the page

layout = dbc.Container([
    dbc.Row(   #row 1 --> Title
        dbc.Col([
            html.Div([
                html.H1('What channel is gonna be used on this purchase?', className="text-sm-center mb-3"),
                html.H3("""
                    Select all the features that you want to use in the prediction.
                    """, className="text-sm-center"),
                html.Hr(
                    style={'color': '#FFFFFF', 'border-color': '#FFFFFF'}
                )
            ])
        ])
    ),
    dbc.Row([
            dbc.Col([
                html.H1('           '),
                html.H4(
                    'Price'
                ),
                dcc.Input(
                    id='price', type='text', placeholder='Price',  min=0, max= 20, step=1, style = {'width': '100%'},
                    className='mb-3', #value=0
                    
                ),
                html.H4(
                    'Month'
                ),
                dcc.Dropdown(
                    id='month', options=[{'label': i, 'value': i} for i in range(1,13)], style = {'color':'#000000'},
                    className='mb-3', value=1
                ),
                html.H4(
                    'Year'
                ),
                dcc.Dropdown(
                    id='year', options=[{'label': i, 'value': i} for i in range(2018,2022)], style = {'color':'#000000'},
                    className='mb-3'
                ),
                html.H4(
                    'Age'
                ),
                dcc.Input(
                    id='age', type='number', placeholder='Age',  min=0, max= 100, step=1, style= {'width': '100%'},
                    className='mb-3'
                ),
                html.H4(
                    'Color'
                ),
                dcc.Dropdown(
                    id='color', options=[{'label': i, 'value': i} for i in encoder_colors.keys()], style = {'color':'#000000'},
                    className='mb-3'
                ),
                html.H4(
                    'Category'
                ),
                dcc.Dropdown(
                    id='category', options=[{'label': i, 'value': i} for i in encoder_index_groups.keys()], style = {'color':'#000000'},
                    className='mb-3'
                ),
                html.H4(
                    'Garment'
                ),
                dcc.Dropdown(
                    id='garment', options=[{'label': i, 'value': i} for i in encoder_garments.keys()], style = {'color':'#000000'},
                    className='mb-3'
                ),
                html.H4(
                    'Model'
                ),
                dcc.Dropdown(
                    id='model', options=['Tree decision', 'rf model' ], style = {'color':'#000000'}, className='mb-3'
                )

            ],width=5),
             dbc.Col([
                dcc.Graph(figure={},id='graph-prediction', style={'width': '100%'}),
                # dbc.Card([
                #     dbc.CardHeader("Prediction", className='text-sm-center'),
                #         dbc.CardBody([
                #             html.H2("Canal predicho", className="card-title text-sm-center",id="card_text5"),
                #             dbc.CardImg(src={}, top=True, style={'width': '35%'},id='channel-img'),
                #     ]),
                # ], className="card text-dark  mb-3 text-sm-center",id='card1', inverse=True
                # ),
                html.H2("Canal predicho", className="card-title text-sm-center",id="card_text5"),
                html.Img(src='',  style={'width': '35%', 'margin-left':'auto', 'margin-right':'auto', 'display':'block'},id='channel-img', className='mb-3'),
            ], width=7),

    ]),
    dbc.Row([
            dbc.Col([
                dbc.Card([
                    dbc.CardHeader("Prediction", className='text-sm-center text-black'),
                        dbc.CardBody([
                            html.H6("Digital channel probability", className="card-title text-sm-center text-black"),
                            html.H5("This is some card text", className=" text-sm-center text-black",id="card_text3")
                        ]),
                    ], className="card text-dark  mb-3 text-sm-center",id='card1', inverse=True, 
                    ),
                ],width= 6),
            dbc.Col([
                dbc.Card([
                    dbc.CardHeader("Prediction", className='text-sm-center text-black'),
                        dbc.CardBody([
                            html.H6("Store channel probability", className="card-title text-sm-center text-black"),
                            html.H5("This is some card text", className="text-sm-center text-black",id="card_text4")
                        ]),
                    ], className="card text-dark  mb-3 text-sm-center",id='card1', inverse=True
                    ),
            ]),
        ]),
])

#############################################################################################################################
@callback(
    Output('card_text3', 'children'),
    Output('card_text4', 'children'),
    Output('card_text5', 'children'),
    Output('graph-prediction', 'figure'),
    Output('channel-img', 'src'),
    [ Input('price', 'value'), 
    Input('month', 'value'), 
    Input('year', 'value'), 
    Input('age', 'value'), 
    Input('color', 'value'), 
    Input('category', 'value'), 
    Input('garment', 'value'),
    Input('model', 'value'),
    ]
)
def prediccion_individual(price:float,month:int,year:int = 2018, age = 25,colors = 'Red',group_indexes = 'Ladieswear',garments = 'Dresses Ladies', model = 'tree'):
    if price == None: 
        new_price=0 
    else:
        try:
            new_price = float(price) 
        except:
            new_price = 0
    if month == None: 
        new_month=5
    elif  month >12:
        new_month=5
    else: new_month = round(month,0)
    if year == None: 
        new_year=2018
    #elif year > 2020: 
    #    new_year=2020
    else: new_year = round(year,0)
    if age == None: 
        new_age=25
    else: new_age = round(age,0)
    
    if colors == None:
        new_color = encoder_colors['Unknown']
    else: 
        new_color = encoder_colors[colors]
        
    if group_indexes == None:
        new_index = encoder_index_groups['Ladieswear']
    else: 
        new_index = encoder_index_groups[group_indexes]
    
    if garments == None:
        new_garment = encoder_garments['Unknown']
    else: 
        new_garment = encoder_garments[garments]
    
    datos = pd.DataFrame(columns = ['price','month','year','age','colors','group_indexes','garments'], data=np.array([new_price,new_month,new_year,new_age,new_color,new_index,new_garment]).reshape(1,-1))
    if model == None:
        loaded_model = get_pickle_data('tree_model.sav')
    elif model == 'tree':
        loaded_model = get_pickle_data('tree_model.sav')
    else:
        loaded_model = get_pickle_data('rf_model.sav')
    probabilities = loaded_model.predict_proba(datos)
    predictions = loaded_model.predict(datos)
    probabilidad_canaldigital = round(probabilities[0][0]*100,2)
    probabilidad_canalpresencial = round(probabilities[0][1]*100,2)
    if predictions == 0:
        clase_predicha = 'Digital Channel'
    else:
        clase_predicha = 'Physical Channel'

    ## pie chart
    probabilites = [round(probabilidad_canaldigital,3),round(probabilidad_canalpresencial,3)]
    labels = ['Digital Channel','Physical Channel']
    fig2 = px.pie(values=probabilites ,names=labels, title='Sales by Channel', hole=.3 )
    fig2.update_layout(title_text='Sales by channel', title_x=0.5, legend_title='Sales Channel' )

    if clase_predicha == 'Digital Channel':
        encoded_image = base64.b64encode(open('/home/crnox95/ds4a_project/data/images/digital_sales.png', 'rb').read())
    else:
        encoded_image = base64.b64encode(open('/home/crnox95/ds4a_project/data/images/presencial_channel.png', 'rb').read())
    
    img = 'data:image/png;base64,{}'.format(encoded_image.decode())
    return str(int(probabilidad_canaldigital)) + '%', str(int(probabilidad_canalpresencial)) + '%' , clase_predicha , fig2, img