#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from math import sqrt
a=int(input("Enter coefficient a:"))
b=int(input("Enter coefficient b:"))
c=int(input("Enter coefficient c:"))

D=b^2-4*a*c

if D > 0:
    x1 = (-b+sqrt(D))/(2*a)
    x2 = (-b-sqrt(D))/(2*a)
    
    print(f"There are two real solutions to the quadratic equation, which are:{x1} and {x2}")
elif D==0:
    x=-b/(2*a)

    print(f"There is one real solution to the quadratic equation, namely: {x}")
          
else:
    print("There are no real solutions to this quadratic equation.")

