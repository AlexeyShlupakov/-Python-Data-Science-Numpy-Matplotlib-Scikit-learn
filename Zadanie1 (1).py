#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np


# In[13]:


a = np.array([[1, 6],
              [2, 8],
              [3, 11],
              [3, 10],
              [1, 7]])


# In[14]:


print(a)


# In[16]:


mean_a = a.mean(axis = 0)


# In[17]:


print(mean_a)


# ## Zadanie2

# In[23]:


a_centered = a - mean_a


# In[24]:


print(a_centered)


# # Zadanie3

# In[25]:


a_centered_sp = a_centered.T[0] @ a_centered.T[1]


# In[26]:


print(a_centered_sp)


# In[27]:


a_centered_sp / (a_centered.shape[0] - 1)


# In[ ]:




