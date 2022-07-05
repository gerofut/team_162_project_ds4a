import dash
import pandas as pd
from dash import html 
import dash_bootstrap_components as dbc
from dash_labs.plugins import register_page
import base64


## Register the page in dash_labs_plugin
register_page(__name__, path="/About")

##### load images
##### David image
image_filename = '/home/crnox95/ds4a_project/data/images/David.jpeg'
encoded_image = base64.b64encode(open(image_filename, 'rb').read())
#### Fredy image
image_filename1 = '/home/crnox95/ds4a_project/data/images/Fredy.jpeg'
encoded_image1 = base64.b64encode(open(image_filename1, 'rb').read())

#### Ricardo image
image_filename2 = '/home/crnox95/ds4a_project/data/images/Rpena 2017.jpg'
encoded_image2 = base64.b64encode(open(image_filename2, 'rb').read())

#### Nicolas image
image_filename3 = '/home/crnox95/ds4a_project/data/images/Nicolas.jpeg'
encoded_image3 = base64.b64encode(open(image_filename3, 'rb').read())

#### Geronimo image
image_filename4 = '/home/crnox95/ds4a_project/data/images/Geronimo.jpeg'
encoded_image4 = base64.b64encode(open(image_filename4, 'rb').read())

#### Daniel image
image_filename5 = '/home/crnox95/ds4a_project/data/images/Daniel.jpg'
encoded_image5 = base64.b64encode(open(image_filename5, 'rb').read())

#### Ariadna image
image_filename6 = '/home/crnox95/ds4a_project/data/images/Ariadna.jpg'
encoded_image6 = base64.b64encode(open(image_filename6, 'rb').read())


##### Define the layout of the page

layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.Div([
                html.H1("TEAM 162 DATA SCIENCE FOR ALL COHORT-6 ", className="text-sm-center display-1"),
                html.H1("About us and where to find us", className="text-sm-center"),
            ])
        ]),
    ]),
    dbc.Row([
        ##Card 1
        dbc.Col([
            dbc.Card([
                dbc.CardImg(src='data:image/jpeg;base64,{}'.format(encoded_image.decode()), top=True),
                dbc.CardBody([
                html.H4("David Alfredo Romero Acosta", className="card-title"),
                html.P(
                    "M Sc. Industrial Engenieer with experience in business inteligence, lean six sigma and business consulting. Data science enthusiast",
                    className="card-text",
                ),
                dbc.Button("View linkedin profile", color="primary", href='https://www.linkedin.com/in/daromaco/'),
                ]),
            ],style={"width": "18rem"}, 
            ),
        ]),
        ## Card 2
        dbc.Col([
            dbc.Card([
                dbc.CardImg(src='data:image/jpeg;base64,{}'.format(encoded_image1.decode()), top=True),
                dbc.CardBody([
                html.H4("Fredy Antonio Salazar Vasquez", className="card-title"),
                html.P(
                    "Master in Computer Science with experience in Data Science an Machine Learning Engineering.",
                    className="card-text",
                ),
                dbc.Button("View linkedin profile", color="primary", href='https://www.linkedin.com/in/fredysalazarv/'),
                ]),
            ],style={"width": "18rem"},
            ),
        ]),
        ### Card 3
        dbc.Col([
            dbc.Card([
                dbc.CardImg(src='data:image/jpeg;base64,{}'.format(encoded_image4.decode()), top=True),
                dbc.CardBody([
                html.H4("Geronimo Valencia", className="card-title"),
                html.P(
                    "Geologist and GIS specialist with experience in seismology and automating tasks with Python. Data science enthusiasts.",
                    className="card-text",
                ),
                dbc.Button("View linkedin profile", color="primary",href='https://www.linkedin.com/in/geronimo-valencia-hoyos-824478192/'),
                ]),
            ],style={"width": "18rem"},
            ),
        ]),
        dbc.Col([
            dbc.Card([
                dbc.CardImg(src='data:image/jpeg;base64,{}'.format(encoded_image2.decode()), top=True),
                dbc.CardBody([
                html.H4("Ricardo Peña", className="card-title"),
                html.P(
                    "Associate Professor at Universidad de Los Andes / Lown Scholar in Cardiovascular Health, T.H. Chan School of Public Health, Harvard University / #Pharmacology, #Public health, #Education, #Gamification enthusiast",
                    className="card-text",
                ),
                dbc.Button("View linkedin profile", color="primary", href='https://www.linkedin.com/in/ricardopena-medicine/'),
                ]),
            ],style={"width": "18rem"},
            ),
        ]),
        ##Card 4
        dbc.Col([
            dbc.Card([
                dbc.CardImg(src='data:image/jpeg;base64,{}'.format(encoded_image3.decode()), top=True),
                dbc.CardBody([
                html.H4("Nicolas Gaona", className="card-title"),
                html.P(
                    "Electronic engineer from Javeriana University with emphasis on digital and signals. With experience in processing and processing signals and programming languages.",
                    className="card-text",
                ),
                dbc.Button("View linkedin profile", color="primary", href="https://www.linkedin.com/in/nicol%C3%A1s-gaona-75ba69213/"),
                ]),
            ],style={"width": "18rem"},
            ),
        ]),
         dbc.Col([
            dbc.Card([
                dbc.CardImg(src='data:image/jpeg;base64,{}'.format(encoded_image5.decode()), top=True),
                dbc.CardBody([
                html.H4("Daniel Restrepo Jimenez", className="card-title"),
                html.P(
                    "M Sc. Industrial Engenieer with experience in data analysis, optimization models and marketing business. Statistics lover",
                    className="card-text",
                ),
                dbc.Button("View linkedin profile", color="primary",href='https://www.linkedin.com/in/daniel-restrepo-jim%C3%A9nez-425439194/'),
                ]),
            ],style={"width": "18rem"},
            ),
        ]),
         dbc.Col([
            dbc.Card([
                dbc.CardImg(src='data:image/jpeg;base64,{}'.format(encoded_image6.decode()), top=True),
                dbc.CardBody([
                html.H4("Ariadna de Avila", className="card-title"),
                html.P(
                    "Master student and professional in Industrial Engineering passionate about data analytics and decision making through optimization models, statistical models and machine learning tools.",
                    className="card-text",
                ),
                dbc.Button("View linkedin profile", color="primary",href='https://www.linkedin.com/in/ariadnadeavila/'),
                ]),
            ],style={"width": "18rem"},
            ),
        ])
    ]) 
], fluid= True)
