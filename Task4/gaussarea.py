import numpy as np
import scipy
from scipy import integrate
import matplotlib.pyplot as plt
from math import *

A = float(input("Please enter value of parameter A:"))
x0 = float(input("Please enter value of parameter x0:"))
sig = float(input("Please enter value of parameter sig:"))
z0 = float(input("Please enter value of parameter z0:"))
a = float(input("Please enter value of the lower bound:"))
b = float(input("Please enter value of the upper bound:"))

def gauss(x, A, x0, sigma, z0):
    return A*np.exp(-(x-x0)**2/(2*sigma**2))+z0

x = np.linspace(-10,10,200)
y = gauss(x,A,x0,sig,z0)

X = x[np.where((a<=x) & (x<=b))] # keeping only a<=x<=b in the domain

area1,error1 = scipy.integrate.quad(gauss,a,b, args = (A,x0,sig,z0,))

plt.rc('text', usetex = True)
plt.plot(x,y, )
plt.fill_between(X,gauss(X,A,x0,sig,z0),0, label = f"The area under the function \n integrated from {a} to {b}: \n {area1:.3f}")
plt.legend(loc = 'upper left')
plt.show()
