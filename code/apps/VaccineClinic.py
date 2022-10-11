import pandas as pd
import numpy as np
from tabulate import tabulate

clinics_df = pd.read_csv(r"..\csv\vaccineclinic.csv")

# checking null value
null = clinics_df.isna().sum()

# type of vaccines provided in clinics sg
types = clinics_df.vaccine
clean = clinics_df.vaccine.drop_duplicates()

# vaccine clinic locations for children
child = clinics_df[clinics_df['vaccine'].str.contains('Children' or 'children')]

# vaccine clinic locations for pfizer/comirnaty
pfz = clinics_df[clinics_df['vaccine'].str.contains('Pfizer' or 'Comirnaty')]

# vaccine clinic locations for sinovac
snv = clinics_df[clinics_df['vaccine'].str.contains('Sinovac')]

# vaccine clinic locations for novavax
nova = clinics_df[clinics_df['vaccine'].str.contains('Novavax')]

# asking users for input
qns = int(input("This is the following datas we can provide for vaccines in singapore:"
                "\n1) type of vaccines provided in singapore"
                "\n2) type of vaccine clinic locations for children"
                "\n3) type of vaccine clinic locations for pfizer/comirnaty"
                "\n4) type of vaccine clinic locations for sinovac"
                "\n5) type of vaccine clinic locations for novavax"
                "\nPlease choose the number for the data you would like to find out more:"))
if qns == 1:
    print(clean)
elif qns == 2:
    print(tabulate(tabular_data=child, headers='keys', tablefmt='fancy_grid'))
elif qns == 3:
    print(tabulate(tabular_data=pfz, headers='keys', tablefmt='fancy_grid'))
elif qns == 4:
    print(tabulate(tabular_data=snv, headers='keys', tablefmt='fancy_grid'))
elif qns == 5:
    print(tabulate(tabular_data=nova, headers='keys', tablefmt='fancy_grid'))
else:
    print("Please enter a valid number")
