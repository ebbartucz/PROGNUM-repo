#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Fibonacci:
    """Class for calculating Fibonacci sequence"""
    def __init__(self,N,M):
        self.N = N
        self.M = M
        
    def fibo(self):
        '''
        The function lists Fibonacci numbers that meet certain requirements.
        Params: N (int), M (int)
        Return: f_m (list) containing all Fibonacci numbers smaller than N and divisible by M.
        '''
        N = self.N
        M = self.M
        
        f = [0]  # list for the Fibonacci numbers smaller than N
        f_m = [] # list for members of f divisible by M

        if M <= 0 or N <= 0:
            return "math error"

        elif 0 < N <=1: # the Fibonacci number smaller than N is zero. Zero is divisible by everything except zero.
            return f

        f.append(1) # if N > 1, 1 can be added to f

        # the next part of the code only runs if the 'if' and 'elif' conditions are not met

        t = f[-1]+f[-2] # t: the next element of the series
        while t < N: 
            f.append(t) 
            t = f[-1]+f[-2]

        for k in f:
            if k%M == 0: # deciding about each element if it is divisible by M
                f_m.append(k) # if yes, we add it to f_m
        return f_m

print(Fibonacci(100,7).fibo()) # the example values

#code should give fibonacci numbers smaller than the Nth term that are divisible by M.
# it is better to define multiple methods inside an object, so here one for f and one for f_m

