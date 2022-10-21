#import dash_core_components as dashCoreComp
#import dash_html_components as dashHTMLComp
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from dash import Dash, html, dcc

from apps.app import server
from apps.app import app
# put filenames here
from apps import MainPage, VaccineRate, VaccineClinic, covid_vaccination_vs_death_ratio,covid_19_retrenchment_analysis, HappinessIndex

dropdownVacc = dbc.DropdownMenu(
    children=[
        dbc.DropdownMenuItem("Vaccine Rates", href="/VaccineRates"),
        dbc.DropdownMenuItem("Vaccine Clinics", href="/VaccineClinics"),
        dbc.DropdownMenuItem("Dataset", href="")
    ],
    nav = True,
    in_navbar = True,
    label = "Vaccinations",
    color='#2AD540',
)

dropdownDeath = dbc.DropdownMenu(
    children=[
        dbc.DropdownMenuItem("Vaccination VS Death Ratios", href="/VaccinationVSDeathRatio"),
        dbc.DropdownMenuItem("Dataset", href="")
    ],
    nav = True,
    in_navbar = True,
    label = "Safety of Vaccines",
    color='#2754D8',
)

dropdownRet = dbc.DropdownMenu(
    children=[
        dbc.DropdownMenuItem("Retrenchment Analysis", href="/RetrenchmentAnalysis"),
        dbc.DropdownMenuItem("Dataset", href="")
    ],
    nav = True,
    in_navbar = True,
    label = "Retrenchment",
    color='#8E38DE',
)

dropdownHappy = dbc.DropdownMenu(
    children=[
        dbc.DropdownMenuItem("Happiness Index", href="/HappinessIndex"),
        dbc.DropdownMenuItem("Dataset", href="")
    ],
    nav = True,
    in_navbar = True,
    label = "Happiness",
    color='#DFB820',
)


navButtons = dbc.Nav(
    children=[
        dbc.Button("Home", color="primary",href="/MainPage", className = "me-1"),
#        dbc.Button("Vaccine Rates", color="primary",href="/VaccineRates",className = "me-1"),
#        dbc.Button("Vaccine Clinics", color="primary",href="/VaccineClinics",className = "me-1"),
#        dbc.Button("Retrenchment Analysis", color="primary",href="/RetrenchmentAnalysis",className = "me-1"),
#        dbc.Button("Vaccination VS Death Ratio", color="primary",href="/VaccinationVSDeathRatio",className = "me-1"),
#        dbc.Button("Happiness Index", color="primary",href="/HappinessIndex",className = "me-1"),
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
                        dbc.Col(dbc.NavbarBrand("COVID-19 Analysis", className="ml-2")),
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
                    [navButtons,dropdownVacc,dropdownDeath,dropdownRet,dropdownHappy], className="ml-auto", navbar=True
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
    elif pathname == '/VaccineClinics':
        return VaccineClinic.layout
    elif pathname == '/RetrenchmentAnalysis':
        return covid_19_retrenchment_analysis.layout
    elif pathname == '/VaccinationVSDeathRatio':
        return covid_vaccination_vs_death_ratio.layout
    elif pathname == '/HappinessIndex':
        return HappinessIndex.layout
    else:
        return MainPage.layout
        #return home.layout or whatever is the landing page here

if __name__ == '__main__':
    app.run_server(debug=True)