#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import numpy as np
from math import *

x = list(range(-5,6,1))
y = []
for i in range(len(x)):
    y.append(cosh(x[i]))
plt.scatter(x, y, label='catenary')
plt.title("Catenary plot using range")
plt.grid()
plt.xlabel("x")
plt.ylabel("cosh(x)")
plt.xticks(fontsize=11)
plt.yticks(fontsize=11)
plt.legend(fontsize=11)
plt.show()

x = np.arange(-5,6,1)
y = np.cosh(x)
plt.scatter(x, y, label='catenary')
plt.title("Catenary plot using arange")
plt.grid()
plt.xlabel("x")
plt.ylabel("cosh(x)")
plt.xticks(fontsize=11)
plt.yticks(fontsize=11)
plt.legend(fontsize=11)
plt.show()



# In[ ]:




