import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from dash.dependencies import Input, Output, State
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
import plotly.express as px
from app import app

# Read retrenchment industry data
df = pd.read_csv(r"..\csv\retrench_industry_yearly.csv")
print("Retrenchment industry data read successfully!")

# Prints the overview of the retrenchment industry data
df.describe

# Prints the count, unique, top, freq of the retrenchment industry data
# Describe function only takes in float or integer values
df['retrench'].describe()

# Prints out a summary of the number of values in each column for the retrenchment industry data
#df.info()

# Read retrenchment industry data with null values, containing '-'
df = pd.read_csv(r"..\csv\retrench_industry_yearly.csv", na_values = ["-"])
#df

# Prints out a summary of the number of missing values, containing '-'
sums = df.isnull().sum()
#print(sums)
#print("Total Missing Values:", sums.sum())

# Make a copy of the original dataframe
# Make a duplicate and make changes from the duplicate set to not make changes to the original dataset
# Drop rows with missing values, containing '-'
df2 = df.copy()
df2=df2.dropna(how='any')

# Prints out a summary of the number of missing values after dropping '-', to ensure that there are no more missing values
sums = df2.isnull().sum()
#print(sums)
#print("Total Missing Values:", sums.sum())

# Counts the number of rows after dropping missing values
#df.info()

# Drops any rows that have 'others' value in the industry columns
df3 = df2.copy()
df3 = df3[(df3.industry1 != 'others') & (df3.industry2 != 'others') & (df3.industry3 != 'others')]

# Counts the number of rows after dropping 'others' value in the industry columns
#df3.info()

# Prints out recent 5 years from 2017 to 2021
df4 = df3.loc[(df3['year'] >= 2017) & (df3['year'] <= 2021)]
#print(df4)

# To export dataframe to csv file after cleaned
# df4.to_csv('retrench_industry_yr_cleaned.csv', index=False)

# Sorts retrench value in ascending order
df5 = df4.sort_values(by = ['retrench'])
#print(df5)

df5["industry1"].nunique()

df5["industry1"].unique()

# Retrieve retrenchment rate by industry type from 2017-2021
df5.groupby(['industry1'])['retrench'].agg('sum')

df8 = df5.groupby(['industry3'])['retrench'].agg('sum')

# Option a). Look at the retrenchment rate by industry before Covid-19
df10 = df5.loc[(df5['year'] >= 2017) & (df5['year'] <= 2019)][['year', 'industry3', 'retrench']]
#print(df10)

# Option b). Look at the retrenchment rate by industry during Covid-19
df12 = df5.loc[df5['year']==2020][['year', 'industry3', 'retrench']]
#print(df12)

# Option c). Look at the retrenchment rate by industry for the post-recovery Covid-19
df14 = df5.loc[df5['year']==2021][['year', 'industry3', 'retrench']]
#print(df14)

df5["industry3"].nunique()

# Asking users for input
options = int(input("Select one of the following options:"
                "\n1) Display retrenchment data by industry type from 2017-2021"
                "\n2) Display industry type in ascending order"
                "\n3) Display retrenchment rate by industry type yearly" 
                "\n4) Display boxplot for retrenchment rate"
                "\n5) Display retrenchment rate by in-depth industry type"
                "\n6) Display bar chart for retrenchment rate in-depth industry type"
                "\n7) Display bar chart for retrenchment rate by in-depth industry type before Covid-19"
                "\n8) Display bar chart for retrenchment rate by in-depth industry type during Covid-19"
                "\n9) Display bar chart for retrenchment rate by in-depth industry type for the post-recovery Covid-19"
                "\nPlease select one of the options to find out more about the retrenchment rate before, during and post of Covid-19:"))

if options == 1:
    print(df4)

elif options == 2:
    print(df5)

elif options == 3:
    # Plot retrenchment rate by industry type from 2017-2021
    # Noticed that amongst the 3 unique industry types, services has the most retrenchment rate
    plt.rcParams['figure.figsize']=(30,9)
    df6 = df5.groupby(['year', 'industry1'])['retrench'].agg('sum').plot.bar(color=['lightsalmon', 'lightblue', 'plum'])
    plt.xticks(rotation='horizontal')
    plt.show()

elif options == 4:
    plt.rcParams['figure.figsize']=(20,5)
    df7 = df5.boxplot(column='retrench', by='industry1')
    plt.show()

elif options == 5:
    print(df8)

elif options == 6:
    # Plot retrenchment rate by industry type from 2017-2021
    # Noticed that amongst the 3 unique industry types, services has the most retrenchment rate
    plt.rcParams['figure.figsize']=(5,25)
    df9 = df5.groupby(['year', 'industry3'])['retrench'].agg('sum').plot.barh(color=['lightblue'])
    plt.xticks(rotation='horizontal')
    plt.show()

elif options == 7:
    # Plot retrenchment rate by industry type before Covid-19
    plt.rcParams['figure.figsize']=(5,25)
    df11 = df10.groupby(['year', 'industry3'])['retrench'].agg('sum').plot.barh(color=['lightblue'])
    plt.xticks(rotation='horizontal')
    plt.show()

elif options == 8:
    # Plot retrenchment rate by industry type during Covid-19
    plt.rcParams['figure.figsize']=(5,25)
    df13 = df12.groupby(['year', 'industry3'])['retrench'].agg('sum').plot.barh(color=['salmon'])
    plt.xticks(rotation='horizontal')
    plt.show()

elif options == 9:
    # Plot retrenchment rate by industry type for the post-recovery Covid-19
    plt.rcParams['figure.figsize']=(5,25)
    df15 = df14.groupby(['year', 'industry3'])['retrench'].agg('sum').plot.barh(color=['plum'])
    plt.xticks(rotation='horizontal')
    plt.show()

else:
    print("Please enter a valid number")


layout = html.Div(children = [
    
    #top text and graph, init below
    html.Div(id="dispGrphRet"),

    #local graph selection, affects the div above this
    html.Div(children=[
        dcc.RadioItems(id="grphChoiceRet",
            options=[
                {'label': 'Retrenchment Data by Industry, 2017-2021', 'value':'RetDataInd' },
                {'label': 'Industry type (Ascending Order)', 'value':'IndTypAsc' },
                {'label': 'Retrenchment Rate by Industry Type Yearly(only this works for now)', 'value':'RetRateYrly' },
                {'label': 'Boxplot for Retrenchment Rate', 'value':'BoxRetRate' },
                {'label': 'Retrenchment Rate by In-depth Industry Type', 'value':'RetRateInDepth' },
                {'label': 'Bar Chart for Retrenchment Rate by In-depth Industry Type', 'value':'BarChartRetRate' },
                {'label': 'Bar Chart for Retrenchment Rate by In-depth Industry Type before Covid-19', 'value':'BarChartRetRateBfC19' },
                {'label': 'Bar Chart for Retrenchment Rate by In-depth Industry Type during Covid-19', 'value':'BarChartRetRateDrC19' },
                {'label': 'Bar Chart for Retrenchment Rate by In-depth Industry Type for post-recovery period of Covid-19', 'value':'BarChartRetRateAfC19' },
            ],
            value = 'RetDataInd',
            labelStyle={'display':'block'}
        )
    ])
])

@app.callback(Output("dispGrphRet","children"), [[Input('grphChoiceRet','value'),]])
def swapDisplay(choice):   
    match choice:
        case 'RetDataInd':
            x = 0
        case 'IndTypAsc':
            x = 0
        case 'RetRateYrly':
            #df6 = df5.groupby(['year', 'industry1'])['retrench'].agg('sum').plot.bar(color=['lightsalmon', 'lightblue', 'plum'])
            #df6 = df5.groupby(['year', 'industry1'])['retrench'].agg('sum')#.plot.bar(color=['lightsalmon', 'lightblue', 'plum'])
            retRate2017to2021 = df5.sort_values('year')
            fig1 = px.bar(retRate2017to2021,  x='industry1', y='retrench', barmode='group', color='industry1', facet_col='year',
                        category_orders={ 'industry1': ['construction','manufacturing','services'],
                                        #'year': ['2017','2018','2019','2020','2021']
                                        },
                        labels=dict(industry1 = 'Industries', retrench = 'Number of Workers Retrenched', construction='Construction')
                        )
            return html.Div(children = [                
                    html.H1(children = "Yearly Retrenchment Rate"),
                    dcc.Graph(figure=fig1)])        
        case 'BoxRetRate':
            x = 0
        case 'RetRateInDepth':
            x = 0
        case 'BarChartRetRate':
            x = 0
        case 'BarChartRetRateBfC19':
            x = 0
        case 'BarChartRetRateDrC19':
            x = 0
        case 'BarChartRetRateAfC19':
            x = 0
        case _:
            return html.Div(children = [                
                    html.H1(children = "Dead with highest rate of vaccination"),
                    dcc.Graph(id= 'displayGraph', figure=fig1)]) 