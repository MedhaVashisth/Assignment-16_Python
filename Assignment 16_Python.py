#!/usr/bin/env python
# coding: utf-8

# In[1]:


years_list = [i for i in range(1997,1997+6)]


# In[2]:


years_list


# In[3]:


years_list[3]


# In[4]:


max(years_list)


# In[5]:


things = list(['mozzarella', 'cinderella','salmonella'])


# In[6]:


things


# In[7]:


for i in things:
    print(i.capitalize())
things


# In[8]:


surprise_list = ["Groucho", "Chico", "Harpo"]


# In[9]:


surprise_list


# In[10]:


surprise_list[-1].lower()


# In[11]:


surprise_list[-1][::-1]


# In[12]:


e2f = {'dog':'chien','cat':'chat','walrus':'morse'}


# In[13]:


e2f['walrus']


# In[14]:


f2e = dict((key,value) for value,key in e2f.items())


# In[15]:


f2e


# In[16]:


f2e['chien']


# In[17]:


e2f.keys()


# In[18]:


life ={'animals':{'cat':['Henri', 'Grumpy', 'Lucy'], 'octopi':'', 'emus':''},
       'plants' :'',
       'other' :'' }


# In[19]:


life


# In[20]:


life.keys()


# In[21]:


life['animals'].keys()


# In[22]:


life['animals'].keys()


# In[ ]:




