from dash import Dash, html, dcc, dash_table
import dash_bootstrap_components as dbc

layout = html.Div(children=[
    #opening, landing
    html.H1(children='Analysis on Covid-19'),

    html.P(children=[
        """
        COVID-19's impacts have spread widely in all directions such as 
        economical damage to various industries. Despite rising COVID-19 
        vaccination rates, hesitancy remains a barrier to full disease 
        immunization. This GUI shows the effects of COVID-19 on 
        retrenchment, well-being, and vaccinations. The goal is to provide 
        the public with a profound understanding of the COVID-19 situation 
        and to encourage them to take vaccines.
        """
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
                        dcc.Link(
                            html.Button('Vaccination Rates Worldwide', 
                                style = {'background-color':'#79E587',
                                        'width':'16rem',
                                        'padding':'0.5rem',
                                },
                            ),
                            href="/VaccineRates",
                            refresh=True
                        )
                    ]),
                    html.Br(),
                    #button 2
                    dbc.Row(children=[
                        dcc.Link(
                            html.Button('Vaccine Clinics in Singapore', 
                                style = {'background-color':'#79E587',
                                        'width':'16rem',
                                        'padding':'0.5rem',
                                },
                            ),
                            href="/VaccineClinics",
                            refresh=True
                        )
                    ]),
                    html.Br(),
                    dbc.Row(children=[
                        dcc.Link(
                            html.Button('Vaccination VS Death rates', 
                                style = {'background-color':'#79E587',
                                        'width':'16rem',
                                        'padding':'0.5rem',
                                },
                            ),
                            href="/VaccinationVSDeathRatio",
                            refresh=True
                        )
                    ]),

                    html.Br(),
                    #button 3 https://github.com/SaltedEggYok/INF1002-assignment-1/tree/main/csv
                    dbc.Row(children=[
                        dcc.Link(
                            html.Button('Dataset', 
                                style = {'background-color':'#79E587',
                                        'width':'16rem',
                                        'padding':'0.5rem',
                                },
                            ),
                            href="https://github.com/SaltedEggYok/INF1002-assignment-1/tree/main/csv",
                            refresh=True
                        )
                    ]),

                ],
                width=4
                ),
                #explanations of the segment
                dbc.Col(children=[
                    html.P(children=['When COVID-19 started, vaccinations are rolled out quickly. This will allow people to take vaccines to increase their immunity to fight against the COVID-19 virus and various sub-variants of COVID-19 such as delta, omicron, Ba.4, Ba.5, and XBB. Many countries are using the strategy of "living with COVID-19". This makes vaccination a requirement for some activities, such as work, concerts, traveling, dine-in at restaurants, and more. To find out more about vaccination rates and vaccine clinics in Singapore, feel free to click and explore!'
                        ]
                    ),
                    ],
                    width=8,
                    style={'border':'2px black solid'},
                )
            ],            
            ),
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
                        dcc.Link(
                            html.Button('Retrenchment Rates', 
                                style = {'background-color':'#B176E8',
                                        'width':'16rem',
                                        'padding':'0.5rem',
                                },
                            ),
                        href="/RetrenchmentAnalysis",
                        refresh=True
                        )
                    ]),
                    html.Br(),
                    #button 2
                    dbc.Row(children=[
                        dcc.Link(
                            html.Button('Dataset', 
                                style = {'background-color':'#B176E8',
                                        'width':'16rem',
                                        'padding':'0.5rem',
                                },
                            ),
                            href="https://github.com/SaltedEggYok/INF1002-assignment-1/tree/main/csv",
                            refresh=True
                        )
                    ]),
                ],
                width=4
                ),
                #explanations of the segment
                dbc.Col(children=[
                    html.P('We want to determine whether there is a strong correlation between the Human Development Index (HDI), Stringency Index (STI), Gross Domestic Product per Capita (GDPCAP), Total Deaths due to COVID-19 (TD) and the Total Cases of COVID-19 (TC).'),
                    ],
                    width=8,
                    style={'border':'2px black solid'}
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
                        dcc.Link(
                            html.Button('Results', 
                                style = {'background-color':'#E4C548',
                                        'width':'16rem',
                                        'padding':'0.5rem',
                                },
                            ),
                        href="/HappinessIndex",
                        refresh = True
                        )
                    ]),
                    html.Br(),
                    #button 2
                    dbc.Row(children=[
                        dcc.Link(
                            html.Button('Dataset', 
                                style = {'background-color':'#E4C548',
                                        'width':'16rem',
                                        'padding':'0.5rem',
                                },
                            ),
                            href="https://github.com/SaltedEggYok/INF1002-assignment-1/tree/main/csv",
                            refresh=True
                        )
                    ]),
                ],
                width=4
                ),
                #explanations of the segment
                dbc.Col(children=[
                    html.P('We plot a Pearson Correlation Heatmap to analyse which of the various factors (GDP per Capita, Social Support, Life Expectancy, Freedom, Generosity, Perception of Corruption) are positively correlated to the Happiness Score.'),
                    ],
                    width=8,
                    style={'border':'2px black solid'}
                )
            ]),

        ]),        
    ]),
])

#app.run_server()
