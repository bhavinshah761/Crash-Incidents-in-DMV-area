#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[29]:


df_Crash_data = pd.read_csv("C:\\Users\\bhavi\\OneDrive\\Desktop\\INFS 580\\Book1.csv")
df_Crash_data


# In[5]:


df_Crash_data.info()


# In[31]:


df_Crash_data = df_Crash_data.rename(columns={'Crash Date/Time':'crash_year'})
df_Crash_data = df_Crash_data.rename(columns={'Local Case Number':'case_num'})
gx = df_Crash_data['crash_year'].str[-4:]
print(gx)


# In[32]:


#pd.to_numeric(gx).astype(int)
gx = gx.astype(str).astype(int)
gx.dtypes


# In[33]:


gx.info()


# In[39]:


bx = df_Crash_data.groupby(gx).case_num.count().reset_index()
print(bx)
yr = np.array(bx['crash_year']).reshape(-1,1)
rn = np.array(bx['case_num']).reshape(-1,1)


# In[45]:


plt.xlabel('Crash Years')
plt.ylabel('Count of Local Case Numbers')
plt.scatter(yr,rn)
plt.show()


# In[46]:


from sklearn.linear_model import LinearRegression
model = LinearRegression()
clf = model.fit(yr,rn)
predictions = model.predict(yr)
plt.plot(yr,predictions,color='green')
plt.xlabel('Crash Years')
plt.ylabel('Count of Local Case Numbers')
plt.show()


# In[44]:


df2 = [[2023],[2024],[2025],[2026]]
predicted_years = model.predict(df2)
print(predicted_years)


# In[ ]:




