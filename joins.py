#! /usr/bin/env python3

# coding: utf-8

# # Joins

# # Introduction

# This Jupyter notebook explores SQL joins using Python.

# ## Left outer join

# In[1]:


import pandas as pd


# In[2]:


#left_table = pd.read_excel('left_table.xlsx', 'Sheet1')
left_table = pd.read_csv('left_table.csv') # prefer csv for very large files


# In[3]:


left_table.head()


# In[4]:


left_table.shape


# In[5]:


left_table.insert(loc=2, column='Desk Location', value='')


# In[6]:


left_table.head()


# In[7]:


left_table.dtypes


# In[8]:


left_table.head()


# In[9]:


#right_table = pd.read_excel('right_table.xlsx', 'Sheet1')
right_table = pd.read_csv('right_table.csv') # prefer csv for very large files


# In[10]:


right_table.head()


# In[11]:


right_table.dtypes


# In[12]:


left_table['Desk Location'] = left_table[['Employee']]    .merge(right_table[['Names', 'Desk Location']],                         left_on='Employee',                          right_on='Names',                          how='left')['Desk Location'].values


# In[13]:


left_table.head(10)


# In[14]:


# These are the 'Employee' that were not assigned a 'Desk Location',
# therefore, the 'Names' is not present or not spelled the same
# in right_table.
left_table = left_table[['ID',                          'Employee',                          'Desk Location']]                       [left_table['Desk Location'].isnull()]


# In[15]:


left_table.head(10)


# In[16]:


# Remove all rows with "NaN" in 'Employee'.
#left_table.dropna(axis=0, how='any', inplace=True)
left_table.dropna(subset=['Employee'], inplace=True)


# In[17]:


# convert 'ID' from a flot to an integer
left_table['ID'] = left_table['ID'].astype(int)


# In[18]:


left_table.head()


# In[19]:


# save the left_table as a csv, don't overwrite the original file
left_table.to_csv('left_table_exceptions.csv')

