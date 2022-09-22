#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd                                                         #to clean and filter data
import numpy as np                                                         #for using data as array
import matplotlib.pyplot as plt                                           #for plotting graph of x,y


# In[2]:


#retrieving and reading CSV using pandas library

world = pd.read_csv(r'vaers_jan_nov_2021.csv')
features = pd.read_csv(r'Features.csv')


#displays up to 50 columns

pd.set_option('display.max_columns', 50)   

#displays up to 200 rows

pd.set_option('display.max_rows', 200)


# In[3]:


features 


# In[4]:


df2 = world


# In[5]:


# grouping people with different doses and count how many deaths in each dose due to vaccination.

count = df2.groupby(['VAX_DOSE_SERIES'])
count['DIED'].value_counts()


# In[6]:


# Sum of people with adverse reaction from each dose group by using RECOVD column.
# RECOVED tell us how many people have recovered. 

count['RECOVD'].value_counts()


# In[7]:


#sum of people with adverse reaction, 1 dose = 172336+152680+104516 = 429532
#sum of people with adverse reaction, 2 dose = 119572+89045+48383 = 257000
#sum of people with adverse reaction, 3 dose = 6217+5922+3556 = 15695


# In[8]:


Number_of_people_with_adverse_reaction = [429532, 257000]
Number_of_people_died_with_adverse_reaction = [7237, 5748]
index = ['1st Dose', '2nd Dose']
df = pd.DataFrame({'Number_of_people_with_adverse_reaction': Number_of_people_with_adverse_reaction,
                   'Number_of_people_died_with_adverse_reaction': Number_of_people_died_with_adverse_reaction}, index=index)
ax = df.plot.bar(rot=0)


# In[9]:


Number_of_people_with_adverse_reaction = [15695]
Number_of_people_died_with_adverse_reaction = [164]
index = ['3rd Dose']
df = pd.DataFrame({'Number_of_people_with_adverse_reaction': Number_of_people_with_adverse_reaction,
                   'Number_of_people_died_with_adverse_reaction': Number_of_people_died_with_adverse_reaction}, index=index)
ax = df.plot.bar(rot=0)


# In[10]:


# assign values to lists  
data = [{'Number_of_people_with_adverse_reaction': 429532, '%_of_people_died_with_adverse_reaction': 1.6}, {'Number_of_people_with_adverse_reaction': 257000, '%_of_people_died_with_adverse_reaction': 2.23},{'Number_of_people_with_adverse_reaction':15695, '%_of_people_died_with_adverse_reaction': 1.04}]  
  
# Creates padas DataFrame by passing  
# Lists of dictionaries and row index.  
dframe = pd.DataFrame(data, index =['1st Dose', '2nd Dose', '3rd Dose'])  
  
# Print the dataframe  
print(dframe)  


# In[11]:


#The death rate is very low (1-2%) despite having symptons and adverse reaction from vaccionation (1 to 3 doses).

