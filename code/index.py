#import dash_core_components as dashCoreComp
#import dash_html_components as dashHTMLComp
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dashBootComp

from dash import html as dashHTMLComp
from dash import dcc as dashCoreComp
#from dash import

from app import server
from app import app
# put filenames here
from apps import MainPage

dropdown = dashBootComp.DropdownMenu(
    children=[
        dashBootComp.DropdownMenuItem("Home", href="/MainPage")
    ],
    nav = True,
    in_navbar = True,
    label = "Explore",
)

navbar = dashBootComp.Navbar(
    dashBootComp.Container(
        [
            dashHTMLComp.A(
                # Use row and col to control vertical alignment of logo / brand
                dashBootComp.Row(
                    [
                        dashBootComp.Col(dashHTMLComp.Img(src="/assets/virus.png", height="30px")),
                        dashBootComp.Col(dashBootComp.NavbarBrand("COVID-19 DASH", className="ml-2")),
                    ],
                    align="center",
                    #no_gutters=True,
                ),
                href="/home",
            ),
            dashBootComp.NavbarToggler(id="navbar-toggler2"),
            dashBootComp.Collapse(
                dashBootComp.Nav(
                    # right align dropdown menu with ml-auto className
                    [dropdown], className="ml-auto", navbar=True
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
app.layout = dashHTMLComp.Div([
    dashCoreComp.Location(id='url', refresh=False),
    navbar,
    dashHTMLComp.Div(id='page-content')
])

@app.callback(Output('page-content', 'children'),
[Input('url','pathname')])
def display_page(pathname):
    if pathname == '/MainPage':
        return MainPage.layout


if __name__ == '__main__':
    app.run_server(debug=True)