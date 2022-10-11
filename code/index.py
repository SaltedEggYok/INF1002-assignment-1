#import dash_core_components as dashCoreComp
#import dash_html_components as dashHTMLComp
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from dash import Dash, html, dcc

from app import server
from app import app
# put filenames here
from apps import MainPage, VaccineRate
import retrenchmentbyindustrytype

dropdown = dbc.DropdownMenu(
    children=[
        dbc.DropdownMenuItem("Dummy", href="/MainPage"),
        dbc.DropdownMenuItem("Vaccine Rate", href="/VaccineRate")
    ],
    nav = True,
    in_navbar = True,
    label = "Explore",
)
navButtons = dbc.Nav(
    children=[
        dbc.Button("Dummy", color="primary",href="/MainPage", className = "me-1"),
        dbc.Button("Vaccine Rates", color="primary",href="/VaccineRates",className = "me-1"),
        dbc.Button("Retrenchment Rates", color="primary",href="/RetrenchmentRates",className = "me-1"),
        #dbc.Button("Primary", color="primary",className = "me-1"),
    ],
    #navbar=True
)

navbar = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                # Use row and col to control vertical alignment of logo / brand
                dbc.Row(
                    [
                        #dbc.Col(html.Img(src="/assets/virus.png", height="30px")), #remove this / replace this
                        dbc.Col(dbc.NavbarBrand("COVID-19 DASH", className="ml-2")),
                    ],
                    align="center",
                    #no_gutters=True, #useless
                ),
                href="/home",
            ),
            dbc.NavbarToggler(id="navbar-toggler2"),
            dbc.Collapse(
                dbc.Nav(
                    # right align dropdown menu with ml-auto className
                    [navButtons], className="ml-auto", navbar=True
                ),
                id="navbar-collapse2",
                navbar=True,
            ),
        ]
    ),
    color="dark",
    dark=True,
    className="mb-4",
)

# embedding the navigation bar
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    navbar,
    html.Div(id='page-content')
])

@app.callback(Output('page-content', 'children'),
[Input('url','pathname')])
def display_page(pathname):
    if pathname == '/MainPage':
        return MainPage.layout
    elif pathname == '/VaccineRates':
        return VaccineRate.layout
    elif pathname == '/RetrenchmentRates':
        return retrenchmentbyindustrytype.layout
    else:
        x = 0
        #return home.layout or whatever is the landing page here

if __name__ == '__main__':
    app.run_server(debug=True)