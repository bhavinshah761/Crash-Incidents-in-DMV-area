#!/usr/bin/env python
# coding: utf-8

# # Jupyter Demo - Group 1

# In[1]:


# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


# Load dataset
crash_data = "C:\\Users\\bhavi\\OneDrive\\Desktop\\Documents\\INFS 580\\Crash_Incidents.csv"
df = pd.read_csv(crash_data)


# In[3]:


print(df.info())


# In[4]:


print(df.head())


# In[5]:


# Pre-processing step
# Checking null values and their counts
null_counts = df.isna().sum()
print(null_counts)


# In[6]:


# Replacing all null values with 0 in the entire dataset
df.fillna(0, inplace=True)


# In[7]:


null_counts = df.isna().sum()
print(null_counts)


# In[8]:


# Generating statistics for numerical columns
print(df.describe())


# #### SQL Analysis with Jupyter

# In[9]:


from pandasql import sqldf


# In[10]:


query = "Select * from df"

df_dql_query = sqldf(query)
df_dql_query.head()


# In[11]:


query = "Select count(*) from df"

df_dql_query = sqldf(query)
df_dql_query.head()


# In[12]:


query = 'Select "Agency Name",count("Local Case Number") from df group by "Agency Name" '

df_dql_query = sqldf(query)
df_dql_query.head(10)


# In[13]:


query = 'Select "ACRS Report Type",count("Local Case Number") from df group by "ACRS Report Type" '

df_dql_query = sqldf(query)
df_dql_query.head(10)


# ### Visualizations

# In[14]:


#creating a line plot to show the trend of incidents over time (e.g., by year or month)
df['Crash Date/Time'] = pd.to_datetime(df['Crash Date/Time'])
df['Year'] = df['Crash Date/Time'].dt.year
incidents_over_time = df['Year'].value_counts().sort_index()
incidents_over_time.plot(kind='line', marker='o')
plt.xlabel("Year")
plt.ylabel("Count")
plt.title("Crash Incidents Over Time")
plt.show()


# In[15]:


#creating a pie chart for ACRS report type
report_type_counts = df['ACRS Report Type'].value_counts()
plt.figure(figsize=(6, 6))
plt.pie(report_type_counts, labels=report_type_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('ACRS Report Type Distribution')
plt.axis('equal')
plt.show()


# In[16]:


#creating a bar plot for top 5 collision types
top_collision_types = df['Collision Type'].value_counts().head(5)
top_collision_types.plot(kind='bar')
plt.xlabel("Collision Type")
plt.ylabel("Count")
plt.title("Top 5 Collision Types")
plt.xticks(rotation=45)
plt.show()


# In[17]:


#creating a histogram for lane number
plt.hist(df['Lane Number'], bins=20, edgecolor='k')
plt.xlabel('Lane Number')
plt.ylabel('Frequency')
plt.title('Histogram of Lane Number')
plt.show()


# In[18]:


#creating a scatterplot for crash incidents
plt.figure(figsize=(10, 8))
plt.scatter(df['Longitude'], df['Latitude'], alpha=0.5, c='b')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('Geographical Distribution of Crash Incidents')
plt.show()


# In[19]:


cross_tab = pd.crosstab(df['Intersection Type'], df['Road Alignment'])
# Creating a heatmap for road alignment and intersection type
plt.figure(figsize=(10, 10))
sns.heatmap(cross_tab, annot=True, fmt='d', cmap='YlGnBu', cbar=True)
plt.title('Intersection Type vs. Road Alignment')
plt.xlabel('Road Alignment')
plt.ylabel('Intersection Type')
plt.show()


# In[ ]:





# In[20]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[21]:


df_crash_data = pd.read_csv("C:\\Users\\bhavi\\OneDrive\\Desktop\\Documents\\INFS 580\\Crash_Incidents.csv")
df_crash_data


# In[22]:


df_crash_data.info()


# In[23]:


df_crash_data = df_crash_data.rename(columns={'Crash Date/Time':'crash_year'})
df_crash_data = df_crash_data.rename(columns={'Local Case Number':'case_num'})
gx = df_crash_data['crash_year'].str[-4:]
print(gx)


# In[24]:


gx = gx.astype(str).astype(int)
gx.dtypes


# In[25]:


gx.info()


# In[26]:


bx = df_crash_data.groupby(gx).case_num.count().reset_index()
print(bx)
yr = np.array(bx['crash_year']).reshape(-1,1)
rn = np.array(bx['case_num']).reshape(-1,1)


# In[27]:


plt.xlabel('Crash Years')
plt.ylabel('Count of Local Case Numbers')
plt.scatter(yr,rn)
plt.show()


# In[28]:


from sklearn.linear_model import LinearRegression
model = LinearRegression()
clf = model.fit(yr,rn)
predictions = model.predict(yr)
plt.plot(yr,predictions,color='red')
plt.xlabel('Crash Years')
plt.ylabel('Count of Local Case Numbers')
plt.show()


# In[29]:


df1 = [[2024],[2025],[2026],[2027]]
predicted_years = model.predict(df1)
print("Predicted Years From 2024 to 2027:\n",predicted_years)


# In[30]:


r_sq = model.score(yr, rn)
print(f"coefficient of determination: {r_sq}")
print(f"intercept: {model.intercept_}")
print(f"slope: {model.coef_}")


# In[ ]:




