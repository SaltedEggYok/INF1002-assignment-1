import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from dash.dependencies import Input, Output, State
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
import plotly.express as px
from app import app

worldvaxrate_df = pd.read_csv(r"..\csv\vaccinerate.csv")

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
layout = html.Div()
layoutOption = 1
"""
# creating user input
qns = int(input("This is the following datas we can provide for vaccination rates:"
                "\n1) top 5 countries with highest vaccinated rate"
                "\n2) top 5 countries with highest fully vaccinated rate"
                "\n3) singapore's vaccination rate"+
                "\n4) bottom 5 countries with lowest vaccinated rate"
                "\n5) bottom 5 countries with lowest fully vaccinated rate"
                "\nPlease choose the number for the data you would like to find out more:"))


if qns == 1:
    plt.figure(figsize=(10, 7))
    plots = sns.barplot(data=top5vaxratesum, x="Country", y="% of population vaccinated")
    for bar in plots.patches:
        plots.annotate(format(bar.get_height(), '.2f'),
                       (bar.get_x() + bar.get_width() / 2,
                        bar.get_height()), ha='center', va='center',
                       size=10, xytext=(0, 8),
                       textcoords='offset points')
    plt.xlabel("Countries", size=14)
    plt.ylabel("percentage of population vaccinated", size=14)
    plt.title("Top 5 vaccinated rate countries")
    plt.show()

elif qns == 2:
    plt.figure(figsize=(10, 7))
    plots = sns.barplot(data=top5fullvaxratesum, x="Country", y="% of population fully vaccinated")
    for bar in plots.patches:
        plots.annotate(format(bar.get_height(), '.2f'),
                       (bar.get_x() + bar.get_width() / 2,
                        bar.get_height()), ha='center', va='center',
                       size=10, xytext=(0, 8),
                       textcoords='offset points')
    plt.xlabel("Countries", size=14)
    plt.ylabel("percentage of population fully vaccinated", size=14)
    plt.title("Top 5 fully vaccinated rate countries")
    plt.show()

elif qns == 3:
    print(sgsum)
elif qns == 4:
    plt.figure(figsize=(10, 7))
    plots = sns.barplot(data=bot5vaxratesumsort, x="Country", y="% of population vaccinated")
    for bar in plots.patches:
        plots.annotate(format(bar.get_height(), '.2f'),
                       (bar.get_x() + bar.get_width() / 2,
                        bar.get_height()), ha='center', va='center',
                       size=10, xytext=(0, 8),
                       textcoords='offset points')
    plt.xlabel("Countries", size=14)
    plt.ylabel("percentage of population vaccinated", size=14)
    plt.title("Bottom 5 fully vaccinated rate countries")
    plt.show()
elif qns == 5:
    plt.figure(figsize=(10, 7))
    plots = sns.barplot(data=bot5fullvaxratesumsort, x="Country", y="% of population fully vaccinated")
    for bar in plots.patches:
        plots.annotate(format(bar.get_height(), '.2f'),
                       (bar.get_x() + bar.get_width() / 2,
                        bar.get_height()), ha='center', va='center',
                       size=10, xytext=(0, 8),
                       textcoords='offset points')
    plt.xlabel("Countries", size=14)
    plt.ylabel("percentage of population fully vaccinated", size=14)
    plt.title("Bottom 5 fully vaccinated rate countries")
    plt.show()
else:
    print("Please enter a valid number")
"""


layout = html.Div(children = [
    
    #top text and graph, init below
    html.Div(id="display-graph"),

    #local graph selection, affects the div above this
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
    ])
])

@app.callback(Output("display-graph","children"), [[Input('graph-choice','value'),]])
def swapDisplay(choice):   
    match choice:
        case 'HVR':
            figure1 = px.bar(top5vaxratesum,  x="Country", y="% of population vaccinated", color="Country", text = "% of population vaccinated")
            figure1.update_traces(textposition = 'outside')
            return html.Div(children = [                
                    html.H1(children = "Top 5 countries with highest rate of vaccination"),
                    dcc.Graph(id= 'displayGraph', figure=figure1)
                    ]
                )
        case 'HFVR':
            figure1 = px.bar(top5fullvaxratesum,  x="Country", y="% of population fully vaccinated", color="Country", text = "% of population fully vaccinated")
            figure1.update_traces(textposition = 'outside')
            return html.Div(children = [                
                    html.H1(children = "Top countries with highest rate of full vaccinations"),
                    dcc.Graph(id= 'displayGraph', figure=figure1)
                    ]
                )
        case 'SVR':
            figure1 = px.bar(top5vaxratesum,  x="Country", y="% of population vaccinated", color="Country", text = "% of population vaccinated",)
            figure1.update_traces(textposition = 'outside')
            return html.Div(children = [                
                    html.H1(children = "TEMP"),
                    dcc.Graph(id= 'displayGraph', figure=figure1)
                    ]
                )        
        case 'LVR':
            figure1 = px.bar(bot5vaxratesumsort,  x="Country", y="% of population vaccinated", color="Country", text = "% of population vaccinated")
            figure1.update_traces(textposition = 'outside')
            return html.Div(children = [                
                    html.H1(children = "Bottom 5 countries with lowest rate of vaccination"),
                    dcc.Graph(id= 'displayGraph', figure=figure1)
                    ]
                )        
        case 'LFVR':
            figure1 = px.bar(bot5fullvaxratesumsort,  x="Country", y="% of population fully vaccinated", color="Country", text = "% of population fully vaccinated")
            figure1.update_traces(textposition = 'outside')
            return html.Div(children = [                
                    html.H1(children = "Bottom countries with lowest rate of full vaccination"),
                    dcc.Graph(id= 'displayGraph', figure=figure1)
                    ]
                )        

        case _:
            return html.Div(children = [                
                    html.H1(children = "Dead with highest rate of vaccination"),
                    dcc.Graph(id= 'displayGraph', figure=figure1)
                    ]
                ) 
        