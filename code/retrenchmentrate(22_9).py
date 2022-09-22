# -*- coding: utf-8 -*-
"""RetrenchmentRate(22/9).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Bm-EoJDQtcgSi7aeetejtJwptY5idIzy
"""

import pandas as pd
import numpy as np
# import matplotlib.pyplot as plt

# Read retrenchment data

df = pd.read_csv(r"..\csv\retrench_occ_yearly.csv")
# print("Retrenchment data read successfully!")

df.describe

null = df.isna().sum()
# print(null)

# Print in the recent 10 years from 2012 to 2021
df2 = df.loc[(df['year'] >= 2012) & (df['year'] <= 2021)]
# print(df2)

# There are 3 different hierarchy positions
df2["occupation"].nunique()

#These are the most common job titles that are being retrenched from 2012 to 2021
df4 = df2["occupation"].unique()

# Selected 2012 data as an example:
# Noticed that the higher-tiered job titles has more people being retrenched as compared to the medium-tiered and low-tiered
# Could be due to the high upkeep positions, that requires them to be paid more than the other tiers

# print(df2[df2["year"] == 2012])

# Sort the retrenchment rate from the lowest to the highest value
df5 = df2.sort_values(by = ['retrench'])
# print(df5)

# Let's take a look at the highest-tier 'professional, managers, executive and technicians', for example:
# As reflected in the data, 2020 is the peak of the pandemic outbreak 
# 2020 has the highest retrenchment rate amongst the recent 10 years while by 2021, it is the lowest (recovered)
df6 = df5[df5['occupation'] == 'professional, managers, executive and technicians']

# to compare all 3 tiers (retrenchment rate) pre and during covid.
#1st which highest, 2nd, 3rd etc..

# Let's take a look at the medium-tier 'clerical, sales and services workers', for example:
# As reflected in the data, 2020 is the peak of the pandemic outbreak 
# 2020 has the highest retrenchment rate amongst the recent 10 years and in 2013, it is the lowest
df7 = df5[df5['occupation'] == 'clerical, sales and services workers']

# Let's take a look at the lowest-tier 'production and transport operators, cleaners and labourers', for example:
# As reflected in the data, 2020 is the peak of the pandemic outbreak 
# 2020 is one of the highest retrenchment rate amongst the recent 10 years while by 2021, it is the lowest (recovered)

# It could be due to the fact of it being under a 'lower-paying' job as compared to the higher-tiered and medium-tiered jobs
# Hence, the lower-tiered job will not have as much impact to companies as compared to the higher-paid ones
# Therefore, letting go of '1 Manager' == letting go of '3 Cleaners'

df8 = df5[df5['occupation'] =='production and transport operators, cleaners and labourers']

# Option a). Look at the retrenchment rate before Covid-19.
df9 = df5.loc[(df['year'] >= 2012) & (df['year'] <= 2019)]

# Option b). Look at the retrenchment rate during Covid-19.
df10 = df5.loc[(df['year'] == 2020)]

# Option c). Look at the retrenchment rate for the post-recovery Covid-19.
df11 = df5.loc[(df['year'] == 2021)]

# Asking users for input
options = int(input("Select one of the following options:"
                "\n1) Display retrenchment data from 2012-2021"
                "\n2) Display job tiers"
                "\n3) Display retrenchment rate in ascending order" 
                "\n4) Display retrenchment rate for professional, managers, executive and technicians"
                "\n5) Display retrenchment rate for clerical, sales and services workers"
                "\n6) Display retrenchment rate for production and transport operators, cleaners and labourers"
                "\n7) Display retrenchment rate before Covid-19"
                "\n8) Display retrenchment rate during Covid-19"
                "\n9) Display retrenchment rate for the post-recovery Covid-19"
                "\nPlease select one of the options to find out more about the retrenchment rate before, during and post of Covid-19:"))

if options == 1:
    print(df2)
elif options == 2:
    print(df4)
elif options == 3:
    print(df5)
elif options == 4:
    print(df6)
elif options == 5:
    print(df7)
elif options == 6:
    print(df8)
elif options == 7:
    print(df9)
elif options == 8:
    print(df10)
elif options == 9:
    print(df11)

else:
    print("Please enter a valid number")
