from msilib import text
from dash import Dash, html, dcc, dash_table
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd

#app = Dash(__name__)

#assume you have a "long-form" data frame
dataFrame = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

figure1 = px.bar(dataFrame,
                 x="Fruit",
                 y="Amount",
                 color="City",
                 barmode="group",
                 text="Amount")
figure1.update_traces(textposition='outside')

layout = html.Div(children=[
    #opening, landing
    html.H1(children='Analysis on Covid-19'),

    html.P(children=[
        'The impacts of COVID-19 have spread widely in every direction,', 
        'as the public appears to have only limited information about how COVID-19 has affected various industries.',
        'Despite the increasing vaccination rates for COVID-19,',
        ' hesitancy continues to be a barrier to the full immunization of the eligible population.',
        ' This report explains the impacts of COVID-19, such as retrenchment, well-being, and vaccinations.',
        ' The goal is to give users a new, profound understanding of the COVID-19 situation and encourage users to take vaccines.',
        ' The report also covers various data sets to create visualizations, such as simple linear regression,',
        ' polynomial regression, bar charts, line charts, heat maps, and tables.',
        ' In addition, an in-depth explanation of the linear regression method,',
        ' such as the accuracy of the correlation. There would also be an additional feature ',
        'of providing vaccine clinic locations in Singapore. Hence, users can derive that the',
        ' retrenchment rate has risen over the last two years of COVID-19, there is a slight ',
        'increase in the happiness score, and vaccines are helpful and encouraged to take to ',
        'prevent high mortality. The findings indicate that continued efforts are needed to ',
        'bolster beliefs about the safety of approved vaccines for COVID-19 and retrenchment.'
        ]
    ),

    #dbc col widths, maximum 12
    #retrenchment, happiness, safety of vaccines, vaccinations
    html.Div(children=[
        dbc.Container(children=[
            #Entire row of elements related to Vaccines
            dbc.Row(children=[
                #left column of buttons
                dbc.Col(children=[
                    #label
                    dbc.Row(children=[
                        dbc.Card(
                            html.H3(children='Vaccinations',),
                            body=True,
                            color='#2AD540',
                            style={'width': '20rem', 
                                    'height':'60%',
                            },
                        ),
                    ]),
                    html.Br(),
                    #button 1
                    dbc.Row(children=[
                        html.Button('Vaccination Rates Worldwide', 
                            style = {'background-color':'#79E587',
                                    'width':'16rem',
                                    'padding':'0.5rem',
                            },
                        ),
                    ]),
                    html.Br(),
                    #button 2
                    dbc.Row(children=[
                        html.Button('Vaccine Clinics in Singapore', 
                            style = {'background-color':'#79E587',
                                    'width':'16rem',
                                    'padding':'0.5rem',
                            },
                        ),
                    ]),
                    html.Br(),
                    #button 3
                    dbc.Row(children=[
                        html.Button('Dataset', 
                            style = {'background-color':'#79E587',
                                    'width':'16rem',
                                    'padding':'0.5rem',
                            },
                        ),
                    ]),

                ],
                width=4
                ),
                #explanations of the segment
                dbc.Col(children=[
                    html.P(children=['To show the vaccination rates in every country, we plot bar charts to show the ranking and percentage for comparison.',
                        html.Br(),
                        'Identify Singapore clinics to take vaccinations, especially for particular age groups, such as children aged 5 to 11 years old,'
                        ]
                    ),
                    ],
                    width=8
                )
            ]),
            html.Br(),
            #Entire row of elements related to Safety of Vaccines
            dbc.Row(children=[
                #left column of buttons
                dbc.Col(children=[
                    #label
                    dbc.Row(children=[
                        dbc.Card(
                            html.H3(children='Safety of Vaccines',),
                            body=True,
                            color='#2754D8',
                            style={'width': '20rem', 
                                    'height':'60%',
                            },
                        ),
                    ]),
                    html.Br(),
                    #button 1
                    dbc.Row(children=[
                        html.Button('Vaccination VS Death rates', 
                            style = {'background-color':'#548FE0',
                                    'width':'16rem',
                                    'padding':'0.5rem',
                            },
                        ),
                    ]),
                    html.Br(),
                    #button 2
                    dbc.Row(children=[
                        html.Button('Dataset', 
                            style = {'background-color':'#548FE0',
                                    'width':'16rem',
                                    'padding':'0.5rem',
                            },
                        ),
                    ]),
                ],
                width=4
                ),
                #explanations of the segment
                dbc.Col(children=[
                    html.P('Our analysis method consists primarily of linear regression as it helps us to identify and understand the correlation within the COVID-19 situation in Singapore, such as mortality and vaccination rates or stringent index and total covid cases in Singapore.'),
                    ],
                    width=8
                )
            ]),
            html.Br(),
            #Entire row of elements related to Retrenchment
            dbc.Row(children=[
                #left column of buttons
                dbc.Col(children=[
                    #label
                    dbc.Row(children=[
                        dbc.Card(
                            html.H3(children='Retrenchment',),
                            body=True,
                            color='#8E38DE',
                            style={'width': '20rem', 
                                    'height':'60%',
                            },
                        ),
                    ]),
                    html.Br(),
                    #button 1
                    dbc.Row(children=[
                        html.Button('Retrenchment Rates', 
                            style = {'background-color':'#B176E8',
                                    'width':'16rem',
                                    'padding':'0.5rem',
                            },
                        ),
                    ]),
                    html.Br(),
                    #button 2
                    dbc.Row(children=[
                        html.Button('Dataset', 
                            style = {'background-color':'#B176E8',
                                    'width':'16rem',
                                    'padding':'0.5rem',
                            },
                        ),
                    ]),
                ],
                width=4
                ),
                #explanations of the segment
                dbc.Col(children=[
                    html.P('We want to determine whether there is a strong correlation between the Human Development Index (HDI), Stringency Index (STI), Gross Domestic Product per Capita (GDPCAP), Total Deaths due to COVID-19 (TD) and the Total Cases of COVID-19 (TC).'),
                    ],
                    width=8
                )
            ]),
            html.Br(),
            #Entire row of elements related to Happiness
            dbc.Row(children=[
                #left column of buttons
                dbc.Col(children=[
                    #label
                    dbc.Row(children=[
                        dbc.Card(
                            html.H3(children='Happiness',),
                            body=True,
                            color='#DFB820',
                            style={'width': '20rem', 
                                    'height':'60%',
                            },
                        ),
                    ]),
                    html.Br(),
                    #button 1
                    dbc.Row(children=[
                        html.Button('Results', 
                            style = {'background-color':'#E4C548',
                                    'width':'16rem',
                                    'padding':'0.5rem',
                            },
                        ),
                    ]),
                    html.Br(),
                    #button 2
                    dbc.Row(children=[
                        html.Button('Dataset', 
                            style = {'background-color':'#E4C548',
                                    'width':'16rem',
                                    'padding':'0.5rem',
                            },
                        ),
                    ]),
                ],
                width=4
                ),
                #explanations of the segment
                dbc.Col(children=[
                    html.P('We plot a Pearson Correlation Heatmap to analyse which of the various factors (GDP per Capita, Social Support, Life Expectancy, Freedom, Generosity, Perception of Corruption) are positively correlated to the Happiness Score.'),
                    ],
                    width=8
                )
            ]),

        ]),        
    ]),
    #happiness
    #    html.Div(children=[]),
    #safety of vaccines
    #    html.Div(children=[]),
    #vaccinations
    #    html.Div(children=[]),
])

#app.run_server()
