from msilib import text
from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

#app = Dash(__name__)

#assume you have a "long-form" data frame
dataFrame = pd.DataFrame({
    "Fruit" : [ "Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount" : [4,1,2,2,4,5],
    "City" : ["SF","SF","SF","Montreal","Montreal","Montreal"]
})

figure1 = px.bar(dataFrame, x = "Fruit", y="Amount", color = "City", barmode = "group",text = "Amount")
figure1.update_traces(textposition = 'outside')

layout = html.Div(children = [
    html.H1(children = 'Hello Dash'),
    html.Div(children= '''Dash: A web application framework for your data'''),
    dcc.Graph(id= 'example-graph', figure=figure1)
])

#app.run_server()




