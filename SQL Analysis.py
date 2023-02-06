#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from pandasql import sqldf


# In[2]:


wd = "C:\\Users\\bhavi\\OneDrive\\Desktop\\Documents\\INFS 580\\Crash_Incidents.csv"


# In[3]:


df = pd.read_csv(wd)


# In[4]:


query = "Select * from df"

df_dql_query = sqldf(query)
df_dql_query.head()


# In[5]:


query = "Select count(*) from df"

df_dql_query = sqldf(query)
df_dql_query.head()


# In[6]:


query = "Select Light,count('Local Case Number') from df group by Light"

df_dql_query = sqldf(query)
df_dql_query.head(20)


# In[7]:


query = 'Select "Agency Name",count("Local Case Number") from df group by "Agency Name" '

df_dql_query = sqldf(query)
df_dql_query.head(20)


# In[8]:


query = 'Select "Collision Type",count("Local Case Number") from df group by "Collision Type" '

df_dql_query = sqldf(query)
df_dql_query.head(20)


# In[9]:


query = 'Select "ACRS Report Type",count("Local Case Number") from df group by "ACRS Report Type" '

df_dql_query = sqldf(query)
df_dql_query.head(20)


# In[ ]:




