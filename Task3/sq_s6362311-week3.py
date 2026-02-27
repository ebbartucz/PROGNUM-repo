#!/usr/bin/env python
# coding: utf-8

# Question 3.1

# In[17]:


masses = [1.9891e+30, 1.8986e+27, 
          5.6846e+26, 1.0243e+26, 8.6810e+25,
          5.9736e+24, 4.8685e+24, 6.4185e+23, 
          3.3022e+23, 7.349e+22, 1.25e22]

masses_new = []
for m in masses:
    if m > 7.349e+22:
        masses_new.append(m)
print(masses_new)

mass=masses[-5:]

print(mass)

avg = sum(mass)/len(mass)

print(avg)


# In[ ]:




