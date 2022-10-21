import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from dash.dependencies import Input, Output, State
from dash import Dash, html, dcc,dash_table
import dash_bootstrap_components as dbc
import plotly.express as px
from apps.app import app

worldvaxrate_df = pd.read_csv("../csv/vaccinerate.csv")

# checking null value
null = worldvaxrate_df.isna().sum()

# vaccinated rate
vaxrate = worldvaxrate_df.loc[:, ["Country", "% of population vaccinated", "% of population fully vaccinated"]]

# top 5 vaccinated rate
top5vaxrate = worldvaxrate_df.nlargest(n=5, columns=['% of population vaccinated'], keep='all')
top5vaxratesum = top5vaxrate.loc[:, ["Country", "% of population vaccinated"]]

# top 5 fully vaccinated rate
top5fullvaxrate = worldvaxrate_df.nlargest(n=5, columns=['% of population fully vaccinated'], keep='all')
top5fullvaxratesum = top5fullvaxrate.loc[:, ["Country", "% of population fully vaccinated"]]

# bottom 5 vaccinated rate
bot5vaxrate = worldvaxrate_df.nsmallest(n=5, columns=['% of population vaccinated'], keep='all')
# filter to show only 2 columns
bot5vaxratesum = bot5vaxrate.loc[:, ["Country", "% of population vaccinated"]]
# sort values in descending order
bot5vaxratesumsort = bot5vaxratesum.sort_values(by="% of population vaccinated", ascending=False)

# bottom 5 fully vaccinated rate
bot5fullvaxrate = worldvaxrate_df.nsmallest(n=5, columns=['% of population fully vaccinated'], keep='all')
# filter to show only 2 columns
bot5fullvaxratesum = bot5fullvaxrate.loc[:, ["Country", "% of population fully vaccinated"]]
# sort values in descending order
bot5fullvaxratesumsort = bot5fullvaxratesum.sort_values(by="% of population fully vaccinated", ascending=False)

# singapore's position
sg = worldvaxrate_df.loc[worldvaxrate_df["Country"] == "Singapore"]
# filter to show singapore's statistic
sgsum = sg.loc[:, ["Country", "% of population vaccinated", "% of population fully vaccinated"]]

#declare layout
layout = html.Div(children = [
    #top text and graph, init below
    html.H1("Vaccination Rates Around the World"),
    html.P("Click to find out more about the world vaccination rate and also Singapore's vaccination rate:"),
    #local graph selection, affects the div above this
    html.Br(),
    html.Div(children=[
        dcc.RadioItems(id="graph-choice",
            options=[
                {'label': 'Highest Vaccinated Rate', 'value':'HVR' },
                {'label': 'Highest Fully Vaccinated Rate', 'value':'HFVR' },
                {'label': 'Singapore\' Vaccination Rate', 'value':'SVR' },
                {'label': 'Lowest Vaccinated Rate', 'value':'LVR' },
                {'label': 'Lowest Fully Vaccinated Rate', 'value':'LFVR' },
            ],
            value = 'HVR',
            labelStyle={'display':'block'}
        )
    ]),
    html.Div(id="display-graph"),    
    
])

@app.callback(Output("display-graph","children"), [[Input('graph-choice','value'),]])
def swapDisplay(choice):
    titleText = ''   
    match choice:
        case 'HVR':
            figure1 = px.bar(top5vaxratesum,  x="Country", y="% of population vaccinated", color="Country", text = "% of population vaccinated")
            #figure1.update_traces(textposition = 'outside')
            figure1.update_yaxes(range=[0,100])
            titleText = 'Top 5 countries with highest rate of vaccination'
        case 'HFVR':
            figure1 = px.bar(top5fullvaxratesum,  x="Country", y="% of population fully vaccinated", color="Country", text = "% of population fully vaccinated")
            #figure1.update_traces(textposition = 'outside')
            figure1.update_yaxes(range=[0,100])
            titleText = 'Top countries with highest rate of full vaccinations'
        case 'SVR':
            figure1 = dash_table.DataTable(
                id = 'table',
                columns = [{"name": i, "id":i}
                            for i in sgsum],
                data = sgsum.to_dict('records'),
                style_header={'backgroundColor' : 'paleturquoise'},
                style_data={'backgroundColor':'lavender'},
                style_cell={'maxWidth': '25rem','height':'auto','whiteSpace':'normal', 'textAlign':'left'},
                fill_width=False
            )
            return html.Div(children = [                
                    html.H4(children = "Vaccination Rate of Singapore"),
                    figure1
                    ]
                )        
        case 'LVR':
            figure1 = px.bar(bot5vaxratesumsort,  x="Country", y="% of population vaccinated", color="Country", text = "% of population vaccinated")
            #figure1.update_traces(textposition = 'outside')
            figure1.update_yaxes(range=[0,100])
            titleText = 'Bottom 5 countries with lowest rate of vaccination'
        case 'LFVR':
            figure1 = px.bar(bot5fullvaxratesumsort,  x="Country", y="% of population fully vaccinated", color="Country", text = "% of population fully vaccinated")
            #figure1.update_traces(textposition = 'outside')
            figure1.update_yaxes(range=[0,100])
            titleText = 'Bottom countries with lowest rate of full vaccination'
        case _:
            titleText = 'Somethig went wrong'
            figure1 = px.bar(pd.DataFrame( { 'x':[1], 'y':[1] } ), x='x',y='y')
  
    return html.Div(children = [                
            html.H4(titleText),
            dcc.Graph(figure=figure1)
            ]
        ) 

        