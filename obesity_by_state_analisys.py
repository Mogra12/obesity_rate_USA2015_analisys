#!/usr/bin/env python
# coding: utf-8

# In[96]:


import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


# In[97]:


dataframe = pd.read_csv("LakeCounty_Health.csv")


# In[98]:


dataframe.drop(['Shape__Area', 'Shape__Length'], axis=1)


# In[99]:


obesity_mean_geral_rate = dataframe[['Obesity']].mean()


# In[ ]:





# In[100]:


northeast_states = [
    "Maine", "Massachusetts", "New Hampshire", "Rhode Island",
    "Vermont"
]
northeast = dataframe[dataframe['NAME'].isin(northeast_states)]
northeast.drop(['Shape__Area', 'Shape__Length'], axis=1)


# In[111]:


northeast_mean_rate = northeast[['Obesity']].mean()
northeast_mean_rate


# In[112]:


midwest_states = [
    "Indiana", "Iowa", "Kansas", "Michigan", "Minnesota", "Missouri",
    "Nebraska", "North Dakota", "Ohio", "South Dakota", "Wisconsin"
]

midwest = dataframe[dataframe['NAME'].isin(midwest_states)]
midwest_mean_rate = midwest[['Obesity']].mean()
midwest_mean_rate


# In[113]:


south_states = [
    "Alabama", "Arkansas", "Delaware", "Florida", "Georgia", "Kentucky",
    "Louisiana", "Maryland", "Mississippi", "North Carolina", "Oklahoma",
    "South Carolina", "Tennessee", "Texas", "Virginia", "West Virginia"
]

south = dataframe[dataframe['NAME'].isin(south_states)]
south_mean_rate = south[['Obesity']].mean()
south_mean_rate


# In[114]:


mountain_states = [
    "Colorado", "Idaho", "Montana", "Nevada", "New Mexico", "Utah", "Wyoming"
]

mountain = dataframe[dataframe['NAME'].isin(mountain_states)]
mountain_mean_rate = south[['Obesity']].mean()
mountain_mean_rate


# In[121]:


pacific_islands_states = [
    "Guam", "American Samoa", "Northern Mariana Islands", "Wake Island"
]

pacific_islands = dataframe[dataframe['NAME'].isin(pacific_islands_states)]
pacific_islands_mean_rate = south[['Obesity']].mean()
pacific_islands_rate


# In[122]:


regional_divisions = ["Northeast", "Midwest", "South", "Mountain States", "Pacific Islands"]

mean_values = [
    float(northeast_mean_rate.iloc[0]),  
    float(midwest_mean_rate.iloc[0]),     
    float(south_mean_rate.iloc[0]),      
    float(mountain_mean_rate.iloc[0]),   
    float(pacific_islands_mean_rate.iloc[0])  
]


# In[107]:


fig1 = px.bar(x=regional_divisions, y=mean_values)
fig1.update_yaxes(title="Tax of Obesity")
fig1.update_xaxes(title="Regions")


# In[108]:



fig2 = go.Figure(data=[go.Pie(labels=regional_divisions, values=mean_values, pull=[0, 0, 0, 0.1, 0.1])])

fig2.update_yaxes(title="Tax of Obesity")
fig2.update_xaxes(title="Regions")
fig2.show()


# ### The regions of _Pacific islands_ and _Montains States_ needs more attencion, because these regions have less states and they have the greatest of obesity of allover the USA. The _South Region_ have the same rate, however is the region with most people and states.

# In[109]:


fig1.show()


# In[ ]:





