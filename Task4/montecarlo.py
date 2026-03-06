#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np

def montecarlo(x,y,a,b,n):
    '''
    The function calculates the integral of a given function.
    Params: x (np.array) elements in the domain of the function
            y (str) the function that needs to be integrated
            a (float) the lower bound
            b (float) the upper bound
            n (int) the number of elements in x
    Return: integral (float): the integral obtained via the Monte Carlo method
    '''
    f = eval(y)
    integral = (b-a)/n*np.sum(f)
    return integral
    
a = float(input("Please input the lower bound:"))
b = float(input("Please input the upper bound:"))
n = 100000
x = np.random.uniform(a,b,100000)
y = str(input("Please input the function you wish to integrate:"))

print(montecarlo(x,y,a,b,n))
# control case:
# f(x) = x, a = 0, b = 1

