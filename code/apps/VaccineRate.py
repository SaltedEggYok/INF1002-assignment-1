import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

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

# creating user input
qns = int(input("This is the following datas we can provide for vaccination rates:"
                "\n1) top 5 countries with highest vaccinated rate"
                "\n2) top 5 countries with highest fully vaccinated rate"
                "\n3) singapore's vaccination rate"
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
