#!/usr/bin/env python
# coding: utf-8

# # Segmenting and Clustering Neighborhoods in Toronto
# 
# <b>IBM Data Science Specialztion - Coursera</b><br>
# Week 3 assignment
# 
# Md Ibtehajul Islam<br>
# Email: iibtehajul@gmail.com<br>
# LinkedIn: islam-md-ibtehajul<br>

# ### Importing the libraries

# In[444]:


import pandas as pd
import numpy as np
import requests
import math
from bs4 import BeautifulSoup


# # Part 1: Web scraping for Toronto neighborhood and build a clean dataframe

# ## Extracting the dataset from the wikipidea link: 

# #### Requesting the link from wikipidea:

# In[455]:


'''
wikipedia_link = 'https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M'
wikipedia_page = requests.get(wikipedia_link)
page= wikipedia_page.text
'''


# ## Scraping the HTML
# The data we want is in a table, with 3 columns PostalCode, Borough and Neighborhood.<br>
# The table contains a list of postal codes in Canada where the first letter is M. Postal codes beginning with M are located within the city of Toronto in the province of Ontario. Only the first three characters are listed, corresponding to the Forward Sortation Area.

# In[445]:


'''
soup = BeautifulSoup(page, 'html.parser')
match = soup.find_all('tr')
results= match[1:-5]
results[-1]
results[0].contents[5].text[0:-1]

records = []
for result in results:
    postalcode = result.contents[1].text
    borough = result.contents[3].text
    neighbourhood = result.contents[5].text[0:-1]
    records.append((postalcode, borough, neighbourhood))
    
df = pd.DataFrame(records, columns=['Postalcode', 'Borough', 'Neighbourhood'])
df.to_csv('List of postal codes of Canada.csv', index=False)

'''


# ## Reading the created csv file

# In[446]:


df = pd.read_csv('List of postal codes of Canada.csv')
df.head()


# ## Data Wrangling: 

# In[447]:


# Replacing all "Not Assigned" to NaN values:
df['Borough'].replace('Not assigned', np.nan, inplace = True)


# In[448]:


df = df.dropna()


# In[449]:


df.shape


# In[450]:


df.head()


# ## Grouping the neighbourhood by Postalcode and Borough

# In[451]:


df = df.groupby(['Postalcode', 'Borough'])['Neighbourhood'].apply(', '.join).reset_index()
df.head()


# ## Deal with Not assigned Neighborhood
# For M7A Queen's Park, there is no neighborhood assigned.We will replace the 'Not assigned' with the value of the corresponding Borough.

# In[452]:


df.iloc[85]


# In[453]:


df_n = df.Neighbourhood == 'Not assigned'
df.loc[df_n, 'Neighbourhood'] = df.loc[df_n, 'Borough']
df[df_n]


# ## Checking the shape of the Dataframe

# In[454]:


df.shape


# In[ ]:




