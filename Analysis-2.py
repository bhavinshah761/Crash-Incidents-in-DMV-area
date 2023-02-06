#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns


# In[3]:


df_data = pd.read_csv("C:\\Users\\bhavi\\OneDrive\\Desktop\\INFS 580\\Non-Motorists_Data.csv")
df_data


# In[16]:


df_data = df_data.rename(columns={'Report Number':'rep_num'})
ax = df_data.groupby(['Pedestrian Type']).rep_num.count().reset_index()
print(ax)
plt.rcParams['figure.figsize'] = [6,4]
ax.plot.bar(x="Pedestrian Type",y="rep_num",color="blue")
plt.xticks(fontsize = 8)
plt.yticks(fontsize = 8)
plt.xlabel('Pedestrian Type',fontsize = 12,fontweight = "bold")
plt.ylabel('Count of Crashes',fontsize = 12,fontweight = "bold")
plt.title('People involved in Crash Accidents',fontsize = 15, fontweight = "bold")
plt.show()


# In[15]:


df_data = df_data.rename(columns={'Report Number':'rep_num'})
ax = df_data.groupby(['At Fault']).rep_num.count().reset_index()
print(ax)
plt.rcParams['figure.figsize'] = [6,4]
ax.plot.bar(x="At Fault",y="rep_num",color="blue")
plt.xticks(fontsize = 8)
plt.yticks(fontsize = 8)
plt.xlabel('At Fault',fontsize = 12,fontweight = "bold")
plt.ylabel('Count of Crashes',fontsize = 12,fontweight = "bold")
plt.title('Fault of Bicyclists involved in Crash Accidents',fontsize = 12, fontweight = "bold")
plt.show()


# In[ ]:




