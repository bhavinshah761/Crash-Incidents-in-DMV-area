#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns
from sklearn.linear_model import LinearRegression


# In[2]:


df_Crash_data = pd.read_csv("C:\\Users\\bhavi\\OneDrive\\Desktop\\Documents\\INFS 580\\Crash_Incidents.csv")
df_Crash_data


# In[3]:


#Data Pre-processing & Cleaning
df_Crash_data.isna().sum()


# In[4]:


#df_Crash_data = df_Crash_data.dropna()
#print(df_Crash_data)


# In[5]:


#Research Qs 1
df_Crash_data = df_Crash_data.rename(columns={'Report Number':'rep_num'})
ax = df_Crash_data.groupby(['Related Non-Motorist']).rep_num.count().reset_index()
print(ax)
plt.rcParams['figure.figsize'] = [6,4]
ax.plot.bar(x="Related Non-Motorist",y="rep_num",color="blue")
plt.xticks(fontsize = 8)
plt.yticks(fontsize = 8)
plt.xlabel('Related Non-Motorist',fontsize = 12,fontweight = "bold")
plt.ylabel('Count of Crashes',fontsize = 12,fontweight = "bold")
plt.title('Non-Motorists involved in Crash Accidents',fontsize = 12, fontweight = "bold")
plt.show()


# In[6]:


#Research Qs 1 & 3
#df_Crash_data = df_Crash_data.rename(columns={'Report Number':'rep_num'})
bx = df_Crash_data.groupby(['At Fault']).rep_num.count().reset_index()
print(bx)
plt.rcParams['figure.figsize'] = [6,4]
bx.plot.bar(x="At Fault",y="rep_num",color="blue")
plt.xticks(fontsize = 8)
plt.yticks(fontsize = 8)
plt.xlabel('Person at Fault',fontsize = 12,fontweight = "bold")
plt.ylabel('Count of Crashes',fontsize = 12,fontweight = "bold")
plt.title('People at fault in Crash Accidents',fontsize = 15, fontweight = "bold")
plt.show()


# In[7]:


df_Crash_data = df_Crash_data.rename(columns={'Crash Date/Time':'crash_year'})
gx = df_Crash_data['crash_year'].str[-4:]
print(gx)
cx = df_Crash_data.groupby(gx).rep_num.count().reset_index()
print(cx)
plt.rcParams['figure.figsize'] = [6,4]
cx.plot.bar(x="crash_year",y="rep_num",color="blue")
plt.xticks(fontsize = 12)
plt.yticks(fontsize = 12)
plt.xlabel('Crash Years')
plt.ylabel('Count of Crashes near Schools')
plt.title('Accidents in School areas',fontsize = 15, fontweight = "bold")
plt.show()


# In[8]:


df_Crash_data = df_Crash_data.rename(columns={'Local Case Number':'case_num'})
df_Crash_data = df_Crash_data.rename(columns={'Lane Number':'lane_num'})
tr = pd.DataFrame(gx)
print(tr)
yr = np.array(tr['crash_year']).reshape(-1,1)
rn = np.array(df_Crash_data['case_num']).reshape(-1,1)


# In[10]:


#Research Qs 2
#df_Crash_data = df_Crash_data.rename(columns={'Report Number':'rep_num'})
dx = df_Crash_data.groupby(['Weather']).rep_num.count().reset_index()
print(dx)
plt.rcParams['figure.figsize'] = [6,4]
dx.plot.bar(x="Weather",y="rep_num",color="blue")
plt.xticks(fontsize = 8)
plt.yticks(fontsize = 8)
plt.xlabel('Weather',fontsize=12,fontweight = "bold")
plt.ylabel('Count of Crashes',fontsize=12,fontweight = "bold")
plt.title('Effect of Weather in Crash Accidents',fontsize = 15, fontweight = "bold")
plt.show()


# In[11]:


#Research Qs 3
#df_Crash_data = df_Crash_data.rename(columns={'Report Number':'rep_num'})
ex = df_Crash_data.groupby(['Driver Substance Abuse']).rep_num.count().reset_index()
print(ex)
plt.rcParams['figure.figsize'] = [11,8]
plt.xticks(size=25)
ex.plot.bar(x="Driver Substance Abuse",y="rep_num",color="blue")
plt.xticks(fontsize = 12)
plt.yticks(fontsize = 12)
plt.xlabel('Driver Substance Abuse',fontweight = "bold")
plt.ylabel('Count of Crashes',fontweight = "bold")
plt.title('Effect of Substance Abuse on Crash Accidents',fontsize = 15, fontweight = "bold")
plt.show()


# In[12]:


#Research Qs 3
#df_Crash_data = df_Crash_data.rename(columns={'Report Number':'rep_num'})
fx = df_Crash_data.groupby(['Traffic Control']).rep_num.count().reset_index()
print(fx)
plt.rcParams['figure.figsize'] = [6,4]
fx.plot.bar(x="Traffic Control",y="rep_num",color="blue")
plt.xticks(fontsize = 12)
plt.yticks(fontsize = 12)
plt.xlabel('Traffic Control',fontweight = "bold")
plt.ylabel('Count of Crashes',fontweight = "bold")
plt.title('Effect of Traffic Control Signals on Crash Accidents',fontsize = 10, fontweight = "bold")
plt.show()


# In[ ]:




