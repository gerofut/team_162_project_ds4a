#libraries
from operator import is_
import dash 
import dash_labs as dl
import dash_bootstrap_components as dbc
from dash import html as html
from dash.dependencies import Input, Output, State
#from callbacks import register_callbacks

# Dash instance declaration
app = dash.Dash(__name__, plugins=[dl.plugins.pages],
                external_stylesheets=[dbc.themes.DARKLY],)
                
# Menu  bottom bar
bottom_bar = dbc.NavbarSimple([
       ## add the logo
    #dbc.Container(
       # [
       #     html.A(
        #        dbc.Row(
         #           [
          #              dbc.Col(html.Img(src='data/images/c1_logo_tagline.svg', height="30px")),
           #         ]
            #    )
            #)
        #]
    #),
    dbc.Button("Sidemenu", outline=True, color="secondary", className="mr-1", id="btn_sidemenu"),
    dbc.NavItem(dbc.NavLink("Home", href="/")),
    dbc.DropdownMenu(
        [
            
            dbc.DropdownMenuItem(page['name'], href="/{}".format(page['name']))
    
    #navigate trougth pages that are created in pages folder

            for page in dash.page_registry.values()
            if page['module'] != 'Page not found'
        ],
        nav=True,
        label="GRAPHICS",
    ), 

    #Aditional buttons in sidebar
    dbc.NavItem(dbc.NavLink("About us", href="/about")),
    dbc.NavItem(dbc.NavLink("Contact us", href="/contact")),
    ],

    brand = 'Team 162 - Data Science for All',
    color = 'danger',
    dark = True,
    fluid = True,
    className = 'menu',
    fixed = 'bottom'
)

########################################################################################
#SIDEBAR

# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 62.5,
    "width": "16rem",
    "height": "100%",
    "z-index": 1,
    "overflow-x": "hidden",
    "transition": "all 0.5s",
    "padding": "0.5rem 1rem",
    "background-color": "#151515",
}

SIDEBAR_HIDEN = {
    "position": "fixed",
    "top": 0,
    "left": "-16rem",
    "bottom": 62.5,
    "width": "16rem",
    "height": "100%",
    "z-index": 1,
    "overflow-x": "hidden",
    "transition": "all 0.5s",
    "padding": "0rem 0rem",
    "background-color": "#151515",
}

# the styles for the main content position it to the right of the sidebar and
# add some padding.
CONTENT_STYLE = {
    "transition": "margin-left .5s",
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
    "background-color": "dark",
}

CONTENT_STYLE1 = {
    "transition": "margin-left .5s",
    "margin-left": "2rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
    "background-color": "dark",
}

sidebar = html.Div(
    [
        dbc.Collapse([
        html.H2("Sidemenu", className="display-4"),
        html.Hr(),
        html.P(
            "Explore all the features designed by TEAM 162", className="lead"
        ),
        dbc.DropdownMenu(
        [
            
            dbc.DropdownMenuItem(page['name'], href="/{}".format(page['name']))
    
    #navigate trougth pages that are created in pages folder

            for page in dash.page_registry.values()
            if page['module'] != 'Page not found'
        ],
        nav=True,
        label="GRAPHICS",
        
    ),
        dbc.NavItem(dbc.NavLink("Prediction models", href="/prediction"))
        ],   


    id="sidebar",
    style=SIDEBAR_STYLE,
    #className='collapse',
    )
    ]
)

# Layout of the app
app.layout = dbc.Container(
    [
        bottom_bar,
        dl.plugins.page_container,
        sidebar,

    ],
    className = 'dbc',
    fluid = True,
)

@app.callback(
    [
        Output("sidebar", "style"),
        Output("_pages_plugin_content", "style"),
        Output('sidebar', 'is_open'),
        
    ],

    [Input("btn_sidemenu", "n_clicks")],
    [   
        State("sidebar", "is_open"),
    ]
)
def toggle_sidebar(n, nclick):
    if n:
        if nclick == "SHOW":
            sidebar_style = SIDEBAR_HIDEN
            page_style = CONTENT_STYLE1
            cur_nclick = "HIDDEN"
        else:
            sidebar_style = SIDEBAR_STYLE
            cur_nclick = "SHOW"
            page_style = CONTENT_STYLE
            
    else:
        sidebar_style = SIDEBAR_STYLE
        cur_nclick = 'SHOW'
        page_style = CONTENT_STYLE

    return sidebar_style, page_style ,  cur_nclick
    


if __name__ == '__main__':
    app.run_server(debug=True)