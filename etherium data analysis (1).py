#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[4]:


dataset=pd.read_csv('ETH-USD.csv')


# In[6]:


dataset.head()


# In[7]:


dataset.head(10)


# In[8]:


dataset.shape


# In[9]:


dataset.tail()


# In[12]:


dataset.columns


# In[13]:


dataset.index


# In[15]:


dataset.nunique()


# In[16]:


dataset.head(10)


# In[20]:


dataset['Open'].value_counts()


# In[21]:


dataset['Open'].dtype


# In[25]:


dataset.head()


# In[26]:


dataset['Low'].dtype


# In[27]:


dataset['High'].dtype


# In[28]:


dataset['Volume'].dtype


# In[29]:


dataset['Date'].dtype


# In[32]:


dataset.info()


# In[ ]:




