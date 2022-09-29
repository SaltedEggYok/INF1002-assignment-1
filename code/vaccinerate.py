import pandas as pd
import numpy as np

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
bot5vaxratesum = bot5vaxrate.loc[:, ["Country", "% of population vaccinated"]]

# bottom 5 fully vaccinated rate
bot5fullvaxrate = worldvaxrate_df.nsmallest(n=5, columns=['% of population fully vaccinated'], keep='all')
bot5fullvaxratesum = bot5fullvaxrate.loc[:, ["Country", "% of population fully vaccinated"]]

# singapore
sg = worldvaxrate_df.loc[worldvaxrate_df["Country"] == "Singapore"]
sgsum = sg.loc[:, ["Country", "% of population vaccinated", "% of population fully vaccinated"]]

qns = int(input("This is the following datas we can provide for vaccination rates:"
                "\n1) top 5 countries with highest vaccinated rate"
                "\n2) top 5 countries with highest fully vaccinated rate"
                "\n3) singapore's vaccination rate"
                "\n4) bottom 5 countries with lowest vaccinated rate"
                "\n5) bottom 5 countries with lowest fully vaccinated rate"
                "\nPlease choose the number for the data you would like to find out more:"))

if qns == 1:
    print(top5vaxratesum)
elif qns == 2:
    print(top5fullvaxratesum)
elif qns == 3:
    print(sgsum)
elif qns == 4:
    print(bot5vaxratesum)
elif qns == 5:
    print(bot5fullvaxratesum)
else:
    print("Please enter a valid number")