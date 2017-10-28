
# coding: utf-8

# In[48]:


player_1 = "r p r p r s p r s p p r r r r p r s r p p s r".split(" ")
player_2 = "s p r s p s p s r p s r p p r r s p r s s p r".split(" ")


# In[49]:


len(player_1)


# In[50]:


len(player_2)


# In[51]:


history_pair_counts = {}
conditional_counts = {}


# In[52]:


for i in range(1, len(player_1)):
    if (player_1[i - 1], player_2[i - 1], player_1[i]) in conditional_counts:
        conditional_counts[(player_1[i - 1], player_2[i - 1], player_1[i])] += 1.0
    else:
        conditional_counts[(player_1[i - 1], player_2[i - 1], player_1[i])] = 1.0
    
    if (player_1[i - 1], player_2[i - 1]) in history_pair_counts:
        history_pair_counts[(player_1[i - 1], player_2[i - 1])] += 1.0
    else:
        history_pair_counts[(player_1[i - 1], player_2[i - 1])] = 1.0
    


# In[53]:


conditional_counts[("r", "r", "r")]


# In[54]:


conditional_counts[("r", "r", "p")]


# In[55]:


history_pair_counts[("r", "r")]


# In[64]:


history_pair_counts[("s", "p")]


# In[65]:


conditional_counts[("s", "p", "r")]


# In[56]:


prob = 1.0
for i in range(1, len(player_1)):
    prob *= (conditional_counts[(player_1[i - 1], player_2[i - 1], player_1[i])] /
                history_pair_counts[(player_1[i - 1], player_2[i - 1])])


# In[59]:


print("%.7f" % prob)


# In[63]:


print("%.12f" % (0.3333**22))


# In[ ]:




