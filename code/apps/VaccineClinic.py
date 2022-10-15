import pandas as pd
import numpy as np
from tabulate import tabulate

from dash import Dash, html, dcc, Input, Output, State, dash_table
import dash_bootstrap_components as dbc
import plotly.express as px
from app import app #not a library, a local file

clinics_df = pd.read_csv(r"..\csv\vaccineclinic.csv")

# checking null value
null = clinics_df.isna().sum()

# type of vaccines provided in clinics sg
types = clinics_df.vaccine
clean = clinics_df.vaccine.drop_duplicates()

#to make a list that has 1,2,3,...,n, should be a better way but....
iterList= []
for i in range(len(clean)):
    iterList.append(i+1)
iterSeries = pd.Series(iterList)
#creating a new df from the series above
clean.index = [i-1 for i in iterSeries ]
frame = {'S/N':iterSeries, 'Vaccine Types': clean}
df_vaccineTypes = pd.DataFrame(frame)

# vaccine clinic locations for children
child = clinics_df[clinics_df['vaccine'].str.contains('Children' or 'children')].sort_values(by=['name'])

# vaccine clinic locations for pfizer/comirnaty
pfz = clinics_df[clinics_df['vaccine'].str.contains('Pfizer' or 'Comirnaty')].sort_values(by=['name'])

# vaccine clinic locations for sinovac
snv = clinics_df[clinics_df['vaccine'].str.contains('Sinovac')].sort_values(by=['name'])

# vaccine clinic locations for novavax
nova = clinics_df[clinics_df['vaccine'].str.contains('Novavax')].sort_values(by=['name'])
"""
# asking users for input
qns = int(input("This is the following datas we can provide for vaccines in singapore:"
                "\n1) type of vaccines provided in singapore"
                "\n2) type of vaccine clinic locations for children"
                "\n3) type of vaccine clinic locations for pfizer/comirnaty"
                "\n4) type of vaccine clinic locations for sinovac"
                "\n5) type of vaccine clinic locations for novavax"
                "\nPlease choose the number for the data you would like to find out more:"))
if qns == 1:
    print(clean)
elif qns == 2:
    print(tabulate(tabular_data=child, headers='keys', tablefmt='fancy_grid'))
elif qns == 3:
    print(tabulate(tabular_data=pfz, headers='keys', tablefmt='fancy_grid'))
elif qns == 4:
    print(tabulate(tabular_data=snv, headers='keys', tablefmt='fancy_grid'))
elif qns == 5:
    print(tabulate(tabular_data=nova, headers='keys', tablefmt='fancy_grid'))
else:
    print("Please enter a valid number")
"""

layout = html.Div(children = [
    
    #top text and graph, init below
    html.Div(id="display-table"),

    #local graph selection, affects the div above this
    html.Div(children=[
        dcc.RadioItems(id="display-choice",
            options=[
                {'label': 'Vaccines Provided in Singapore', 'value':'vaxInSG' },
                {'label': 'Available Vaccination Locations for Children', 'value':'locForChildren' },
                {'label': 'Available Vaccination Locations with Pfizer/Comirnaty', 'value':'locPfizerComirnaty'},
                {'label': 'Available Vaccination Locations with Sinovac', 'value':'locSinovac' },
                {'label': 'Available Vaccination Locations with Novavax', 'value':'locNovavax' },
            ],
            value = 'vaxInSG',
            labelStyle={'display':'block'}
        )
    ])
])


@app.callback(Output("display-table","children"), [[Input('display-choice','value'),]])
def swapDisplay(choice):   
    match choice:
        case 'vaxInSG':
            header = html.H4("Vaccines Provided in Singapore")
            df_pointer = df_vaccineTypes
        case 'locForChildren':
            header = html.H4("Available Clinic Locations for Children")
            df_pointer = child
        case 'locPfizerComirnaty':
            header = html.H4("Available Clinic Locations for Pfizer")
            df_pointer = pfz
        case 'locSinovac':
            header = html.H4("Available Clinic Locations for Sinovac")
            df_pointer = snv
        case 'locNovavax':
            header = html.H4("Available Clinic Locations for Novavax")
            df_pointer = nova
    fig1 = dash_table.DataTable(
            id = 'table',
            columns = [{"name": i, "id":i}
                        for i in df_pointer],
            data = df_pointer.to_dict('records'),
            style_cell=dict(textAlign='left'),
            style_header=dict(backgroundColor = "paleturquoise"),
            style_data=dict(backgroundColor = "lavender")
        )
    return html.Div(children=[
        header,
        fig1,
    ])
        