#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# importing packages
import pandas as pd
import numpy as np
import matplotlib as plt
import seaborn as sns


# In[ ]:


# defining data frame and opening csv file with pandas

df1 = pd.read_csv(r'G:\Python projects\Egypt GDP\df1.csv')
df1


# In[ ]:


# droping indicies 0-1 and redefining dataframe

df1 = df1.drop(range(0,5))
df1


# In[ ]:


# dropping years 1960-2009 as they don't sreve a purpose for this analysis

df1 = df1.drop(df1.columns.to_series()["1960":"2009"], axis=1)
df1


# In[ ]:


# dropping indicator code

df1 = df1.drop(columns = "Indicator Code")
df1


# In[ ]:


# dropping index 5

df1 = df1.drop(5)
df1


# In[ ]:


# dropping index 8, not enough data to include in the analysis

df1 = df1.drop(8)
df1


# In[ ]:


# resetting index for better clarification

df1 = df1.reset_index(drop=True)
df1


# In[ ]:


df1


# In[ ]:


import random
from matplotlib import pyplot as plt 
import numpy as np 
from matplotlib.animation import FuncAnimation 

labels = ['Agricultural', 'Industrial', 'Services']
data = np.array([[13.340759, 35.784518, 46.232720],
 [13.869105, 35.951718, 46.232720],
 [11.272765, 39.251305, 51.771637],
 [11.274350, 39.886960, 52.300742],
 [11.337704, 39.890333, 52.320991],
 [11.394063, 36.630206, 53.170551],
 [11.769318, 32.455953, 54.483280],
 [11.485285, 33.750764, 53.240873],
 [11.225000, 35.623446, 50.471695],
 [11.567609, 32.009145, 51.760507]])
# explode = (0, 0.1, 0, 0) 
years = [2010 + i  for i in range(11)]

plot_steps = np.array([data[0]])
last_data = data[0]
for i in range(1, len(data)):
    diff = data[i] - last_data
    diff /= 100
    for j in range(101):
        plot_steps = np.append(plot_steps, [last_data + diff * j], 0)
    last_data = data[i]

# print(plot_steps)

years = iter(years)
year = next(years)
for i, step in enumerate(plot_steps):
    if i % 100 == 0:
        year = next(years)
    plt.xlim(0, 100)
    plt.barh(labels, step, color = ["green", "blue", "red"])
    plt.text(0.8, 0.2, year, fontsize = 14)
    plt.pause(0.01)
    plt.clf()
plt.show()


# In[ ]:


df2 = pd.read_csv(r'G:\Python projects\Egypt GDP\GDP-Year.csv')
df2


# In[ ]:





# In[ ]:


import matplotlib.pyplot as plt

ax = df2.plot(x = 'Year', y = 'GDP Per Capita USD', title = "GDP Per Capita - Egypt (2010-2020)")
ax.set_xlabel("Year")
ax.set_ylabel("GDP Per Capita USD")
plt.show()


# In[ ]:




