# -*- coding: utf-8 -*-
"""INF1003 Python Project_Osama Rasheed Khan.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1WzN_NXJdjQR8y9x2-rtqPObud67XYeb6
"""

# import libraries
import numpy as np # Linear Algebra
import pandas as pd # Data processing for csv file (read or write into a csv file)
import seaborn as sns # Data Visualisations
from matplotlib import pyplot as plt # Creating data plots
import statsmodels.api as sm # Statistical Analysis
from statsmodels.formula.api import ols # Ordinary Least Squares used to evaluate linear regression models for predictions

from dash import Dash, html, dcc, Input, Output, State, dash_table
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objects as go

# Read csv files from google drive
#from google.colab import drive
#drive.mount('/content/drive')

import os

#def myfunction(data):
#  print(data)

#dir = '/content/drive/MyDrive/WHR and Covid 19 datasets'

#for file in os.listdir(dir):
#  if file.endswith(".csv"):
#    myfunction(file)

# DATA CLEANING

# Read Data for WHR 2018
df18 = pd.read_csv('../csv/2018.csv')

#df18.head()

#df18.isnull().sum()

df18 = df18.rename(columns = {'Country or region': 'Country', 'Score': 'Score 2018', 'Healthy life expectancy': 'Life expectancy'})

#df18.head()

# Read Data for WHR 2019
df19 = pd.read_csv('../csv/2019.csv')

#df19.head()

#df19.isnull().sum()

df19 = df19.rename(columns = {'Country or region': 'Country','Score': 'Score 2019', 'Healthy life expectancy': 'Life expectancy'})

#df19.head()

# Read Data for WHR 2020
df20 = pd.read_csv('../csv/2020.csv')

#df20.head()

#df20.isnull().sum()

df20 = df20.rename(columns = {'Country name': 'Country', 'Ladder score': 'Score 2020','Healthy life expectancy': 'Life expectancy'})

#df20.head()

# Read Data for WHR 2021
df21 = pd.read_csv('../csv/2021.csv')

#df21.head()

#df21.isnull().sum()

df21 = df21.rename(columns = {'Country name': 'Country', 'Ladder score': 'Score 2021','Healthy life expectancy': 'Life expectancy'})

#df21.head()

# Read Data for WHR COVID Data
dfCovid = pd.read_csv('../csv/WHRCovid21.csv')

#dfCovid.head()

dfCovid = dfCovid.rename(columns = {'Country name': 'Country'})

#dfCovid.head()

# DATA ANALYSIS

#WHR 2018
df18_head = df18.head(10)
df18_tail = df18.tail(10)

ct_df18 = pd.concat([df18_head, df18_tail])

#print(ct_df18)

# Display top 10 and botom 10 countries Happiness Scores for 2018
#plt.figure(figsize = (35,8)) # Adjust size of plot for it to be read
#sns.set(font_scale=1.2)
#ax18 = sns.barplot(x = "Country", y = "Score 2018", data = ct_df18, palette = "brg_r")

#for p in ax18.patches:
#  ax18.text(p.get_x() + p.get_width()/2., p.get_height(), '{0:.3f}'.format(p.get_height()), fontsize = 12, color = 'maroon', ha = 'center', va = 'bottom')

fig2018head = px.bar(data_frame=df18_head, x = 'Country', y= 'Score 2018',text = 'Score 2018', 
                    color = 'Country', title='Top 10 Happiest Countries in 2018',text_auto='.2f',
                    labels={'Country':'Top Countries in 2018'})
fig2018head.update_traces(textposition = 'outside')
fig2018head.update_yaxes(range=[0,10])
fig2018tail = px.bar(data_frame=df18_tail, x = 'Country', y= 'Score 2018',text = 'Score 2018', 
                    color = 'Country', title='Bottom 10 Happiest Countries in 2018',text_auto='.2f',
                    labels={'Country':'Bottom Countries in 2018'})
fig2018tail.update_traces(textposition = 'outside')
fig2018tail.update_yaxes(range=[0,10])

#WHR 2019
df19_head = df19.head(10)
df19_tail = df19.tail(10)

ct_df19 = pd.concat([df19_head, df19_tail])

#print(ct_df19)

# Display top 10 and botom 10 countries Happiness Scores for 2019
#plt.figure(figsize = (35,8)) # Adjust size of plot for it to be read
#sns.set(font_scale=1.2)
#ax19 = sns.barplot(x = "Country", y = "Score 2019", data = ct_df19, palette = "brg_r")

#for p in ax19.patches:
#  ax19.text(p.get_x() + p.get_width()/2., p.get_height(), '{0:.3f}'.format(p.get_height()), fontsize = 12, color = 'maroon', ha = 'center', va = 'bottom')

fig2019head = px.bar(data_frame=df19_head, x = 'Country', y= 'Score 2019',text = 'Score 2019', 
                    color = 'Country', title='Top 10 Happiest Countries in 2019',text_auto='.2f',
                    labels={'Country':'Top Countries in 2019'})
fig2019head.update_traces(textposition = 'outside')
fig2019head.update_yaxes(range=[0,10])
fig2019tail = px.bar(data_frame=df19_tail, x = 'Country', y= 'Score 2019',text = 'Score 2019',
                    color = 'Country', title='Bottom 10 Happiest Countries in 2019',text_auto='.2f',
                    labels={'Country':'Bottom Countries in 2019'})
fig2019tail.update_traces(textposition = 'outside')
fig2019tail.update_yaxes(range=[0,10])

#WHR 2020
df20_head = df20.head(10)
df20_tail = df20.tail(10)

ct_df20 = pd.concat([df20_head, df20_tail])

#print(ct_df20)

# Display top 10 and botom 10 countries Happiness Scores for 2020
#plt.figure(figsize = (35,8)) # Adjust size of plot for it to be read
#sns.set(font_scale=1.2,)
#ax20 = sns.barplot(x = "Country", y = "Score 2020", data = ct_df20, palette = "brg_r")

#for p in ax20.patches:
#  ax20.text(p.get_x() + p.get_width()/2., p.get_height(), '{0:.3f}'.format(p.get_height()), fontsize = 12, color = 'maroon', ha = 'center', va = 'bottom')

fig2020head = px.bar(data_frame=df20_head, x = 'Country', y= 'Score 2020',text = 'Score 2020', 
                    color = 'Country', title='Top 10 Happiest Countries in 2020',text_auto='.2f',
                    labels={'Country':'Top Countries in 2020'})
fig2020head.update_traces(textposition = 'outside')
fig2020head.update_yaxes(range=[0,10])
fig2020tail = px.bar(data_frame=df20_tail, x = 'Country', y= 'Score 2020',text = 'Score 2020', 
                    color = 'Country', title='Bottom 10 Happiest Countries in 2020',text_auto='.2f',
                    labels={'Country':'Bottom Countries in 2020'})
fig2020tail.update_traces(textposition = 'outside')
fig2020tail.update_yaxes(range=[0,10])

#WHR 2021
df21_head = df21.head(10)
df21_tail = df21.tail(10)

ct_df21 = pd.concat([df21_head, df21_tail])

#print(ct_df21)

# Display top 10 and botom 10 countries Happiness Scores for 2021
#plt.figure(figsize = (35,8)) # Adjust size of plot for it to be read
#sns.set(font_scale=1.2)
#ax21 = sns.barplot(x = "Country", y = "Score 2021", data = ct_df21, palette = "brg_r")

#for p in ax21.patches:
#  ax21.text(p.get_x() + p.get_width()/2., p.get_height(), '{0:.3f}'.format(p.get_height()), fontsize = 12, color = 'maroon', ha = 'center', va = 'bottom')

fig2021head = px.bar(data_frame=df21_head, x = 'Country', y= 'Score 2021',text = 'Score 2021', 
                    color = 'Country', title='Top 10 Happiest Countries in 2021',text_auto='.2f',
                    labels={'Country':'Top Countries in 2021'})
fig2021head.update_traces(textposition = 'outside')
fig2021head.update_yaxes(range=[0,10])
fig2021tail = px.bar(data_frame=df21_tail, x = 'Country', y= 'Score 2021',text = 'Score 2021', 
                    color = 'Country', title='Bottom 10 Happiest Countries in 2021',text_auto='.2f',
                    labels={'Country':'Bottom Countries in 2021'})
fig2021tail.update_traces(textposition = 'outside')
fig2021tail.update_yaxes(range=[0,10])

# FIND CORRELATION

# Drop Overall rank column
df19_rev = df19.drop(columns = ['Overall rank'])

# Correlation heatmap for WHR 2019
#plt.figure(figsize = (15,8))
#sns.set(font_scale=2.6)
#ax_corr19 = sns.heatmap(df19_rev.corr(), annot = True, vmin = -1, vmax = 1, center = 0,annot_kws={"size": 30}, cmap = 'YlGnBu')

figHeatmap19 = px.imshow(df19_rev.corr(), title='2019 Pearson Correlation Heatmap',text_auto='.2f',range_color=[-1,1])
#figHeatmap.show()

# Merge df19 and df20 with dfCovid

df_merge19 = pd.merge(df19, dfCovid, how = "outer", on = ["Country"])

df_merge20 = pd.merge(df20, dfCovid, how = "outer", on = ["Country"])

# Merge all WHR datasets to find out happiness score averages throughout COVID 19 period
h1 = pd.merge(df18, df19, how = 'outer', on = ['Country'])
h2 = pd.merge(df20, df21, how = 'outer', on = ['Country'])

df_WHR = pd.merge(h1, h2, how = 'outer', on = ['Country'])

df_WHR = df_WHR.filter(like = 'Score')

#df_WHR.head()

# Average World Happines Score 
df_WHR = df_WHR.mean()
#df_WHR.head()

# Plot Average World Happiness Score Bar chart
#sns.set(font_scale=1)
#df_WHR.plot(x = ['Score 2018', 'Score 2019', 'Score 2020', 'Score 2021'], title = 'Average World Happiness Score', ylabel = 'Score', kind = 'bar', color = 'aquamarine')

figWHR = px.bar(data_frame=df_WHR, 
                y=[df_WHR[0],df_WHR[1],df_WHR[2],df_WHR[3]], 
                text=[df_WHR[0],df_WHR[1],df_WHR[2],df_WHR[3]],
                title='Average World Happiness Score',
                text_auto='.3f',
                labels={'index':'', 'y':'Average Happiness Score'})
figWHR.update_traces(textposition = 'outside')
figWHR.update_yaxes(range=[0,10])

#df19.head()

#df20.head()

# FIND CORRELATION

# Drop Overall rank column
df20_rev = df20.drop(columns = ['Regional indicator', 'upperwhisker', 'lowerwhisker', 'Explained by: Log GDP per capita', 'Explained by: Social support', 'Explained by: Healthy life expectancy', 'Explained by: Freedom to make life choices', 'Explained by: Generosity', 'Explained by: Perceptions of corruption', 'Dystopia + residual', 'Ladder score in Dystopia', 'Standard error of ladder score'])

# Correlation heatmap for WHR 2020
#plt.figure(figsize = (15,8))
#sns.set(font_scale=2.6)
#ax_corr20 = sns.heatmap(df20_rev.corr(), annot = True, vmin = -1, vmax = 1, center = 0,annot_kws={"size": 30}, cmap = 'YlGnBu')

figHeatmap20 = px.imshow(df20_rev.corr(), title='2020 Pearson Correlation Heatmap', text_auto='.2f',range_color=[-1,1])

# SINGAPORE WHR DATA

df18sg = df18[df18['Country'] == 'Singapore']

#print(df18sg)


layout = html.Div(children=[
    html.H1(children=[
        "World Happiness Index"
    ]),
    html.H4(children=['2018'],style={'textAlign':'center'}),
    dbc.Row(children=[
      dbc.Col(children=[
        html.Div(children=[
            dcc.Graph(figure = fig2018head),
        ])
      ],
        width=6,
      ),
      dbc.Col(children=[
        html.Div(children=[
            dcc.Graph(figure = fig2018tail),
        ])
      ],
      width=6,
      ),      
    ]),
    html.H4(children=['2019'],style={'textAlign':'center'}),
    dbc.Row(children=[
      dbc.Col(
        html.Div(children=[
            dcc.Graph(figure = fig2019head),
        ]),
      ),
      dbc.Col(
        html.Div(children=[
            dcc.Graph(figure = fig2019tail),
        ]),
      ),      
    ]),
    html.H4(children=['2020'],style={'textAlign':'center'}),
    dbc.Row(children=[
      dbc.Col(
        html.Div(children=[
            dcc.Graph(figure = fig2020head),
        ]),
      ),
      dbc.Col(
        html.Div(children=[
            dcc.Graph(figure = fig2020tail),
        ]),
      ),      
    ]),
    html.H4(children=['2021'],style={'textAlign':'center'}),
    dbc.Row(children=[
      dbc.Col(
        html.Div(children=[
            dcc.Graph(figure = fig2021head),
        ]),
      ),
      dbc.Col(
        html.Div(children=[
            dcc.Graph(figure = fig2021tail),
        ]),
      ),      
    ]),
    dbc.Row(children=[
      dbc.Col(
        html.Div(children=[
            dcc.Graph(figure = figHeatmap19),
        ]),
      ),
      dbc.Col(
        html.Div(children=[
            dcc.Graph(figure = figHeatmap20),
        ]),
      ),      
    ]),
    html.Div(children=[
        dcc.Graph(figure = figWHR),
    ]),
])