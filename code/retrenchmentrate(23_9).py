import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Read retrenchment data

df = pd.read_csv(r"..\csv\retrench_occ_yearly.csv")
# print("Retrenchment data read successfully!")

df.describe

# Prints the count, mean, std, min, lowerQ, median, upperQ, max
# Describe function only takes in float or integer values
df['retrench'].describe()

null = df.isna().sum()
# print(null)

# Print in the recent 10 years from 2012 to 2021
df2 = df.loc[(df['year'] >= 2017) & (df['year'] <= 2021)]
# print(df2)

# There are 3 different hierarchy positions
df2["occupation"].nunique()

#These are the most common job titles that are being retrenched from 2012 to 2021
df4 = df2["occupation"].unique()

# Selected 2012 data as an example:
# Noticed that the higher-tiered job titles has more people being retrenched as compared to the medium-tiered and low-tiered
# Could be due to the high upkeep positions, that requires them to be paid more than the other tiers

# print(df2[df2["year"] == 2017])

# Sort the retrenchment rate from the lowest to the highest value
df5 = df2.sort_values(by = ['retrench'])
# print(df5)

# Let's take a look at the highest-tier 'professional, managers, executive and technicians', for example:
# As reflected in the data, 2020 is the peak of the pandemic outbreak 
# 2020 has the highest retrenchment rate amongst the recent 10 years while by 2021, it is the lowest (recovered)
df6 = df5[df5['occupation'] == 'professional, managers, executive and technicians']

# Let's take a look at the medium-tier 'clerical, sales and services workers', for example:
# As reflected in the data, 2020 is the peak of the pandemic outbreak 
# 2020 has the highest retrenchment rate amongst the recent 10 years while by 2021, it is the lowest (recovered)
df7 = df5[df5['occupation'] == 'clerical, sales and services workers']

# Let's take a look at the lowest-tier 'production and transport operators, cleaners and labourers', for example:
# As reflected in the data, 2020 is the peak of the pandemic outbreak 
# 2020 is one of the highest retrenchment rate amongst the recent 10 years while by 2021, it is the lowest (recovered)

# It could be due to the fact of it being under a 'lower-paying' job as compared to the higher-tiered and medium-tiered jobs
# Hence, the lower-tiered job will not have as much impact to companies as compared to the higher-paid ones
# Therefore, letting go of '1 Manager' == letting go of '3 Cleaners'

df8 = df5[df5['occupation'] =='production and transport operators, cleaners and labourers']

# Option a). Look at the retrenchment rate before Covid-19.
df9 = df5.loc[(df['year'] >= 2017) & (df['year'] <= 2019)]

# Option b). Look at the retrenchment rate during Covid-19.
df10 = df5.loc[(df['year'] == 2020)]

# Option c). Look at the retrenchment rate for the post-recovery Covid-19.
df11 = df5.loc[(df['year'] == 2021)]

# Created a boxplot to help me identify an outlier

# It could be due to the fact of it being under a 'lower-paying' job as compared to the higher-tiered and medium-tiered jobs
# Hence, the lower-tiered job will not have as much impact to companies as compared to the higher-paid ones
# Therefore, letting go of '1 Manager' == letting go of '3 Cleaners'

# Asking users for input
options = int(input("Select one of the following options:"
                "\n1) Display retrenchment data from 2017-2021"
                "\n2) Display job tiers"
                "\n3) Display retrenchment rate in ascending order" 
                "\n4) Display retrenchment rate for professional, managers, executive and technicians"
                "\n5) Display retrenchment rate for clerical, sales and services workers"
                "\n6) Display retrenchment rate for production and transport operators, cleaners and labourers"
                "\n7) Display retrenchment rate before Covid-19"
                "\n8) Display retrenchment rate during Covid-19"
                "\n9) Display retrenchment rate for the post-recovery Covid-19"
                "\n10) Display boxplot for retrenchment rate"
                "\n11) Display bar chart for retrenchment rate"
                    
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
elif options == 10:
    # Created a boxplot to help me identify an outlier
    # It could be due to the fact of it being under a 'lower-paying' job as compared to the higher-tiered and medium-tiered jobs
    # Hence, the lower-tiered job will not have as much impact to companies as compared to the higher-paid ones
    # Therefore, letting go of '1 Manager' == letting go of '3 Cleaners'
    plt.rcParams['figure.figsize']=(20,7)
    df5.boxplot(column='retrench', by='occupation')
    plt.show()
elif options == 11:
    # Let's take a look at the retrenchment rate over the years by occupation
    sns.set(style="whitegrid")
    sns.barplot(data=df5, x="year", y="retrench", hue="occupation", palette="pastel")
    plt.show()
else:
    print("Please enter a valid number")
