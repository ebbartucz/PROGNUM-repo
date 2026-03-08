import numpy as np
from numpy import sin, cos, exp, pi
import scipy
from scipy import integrate

while True: # endless loop inserted after requiring input to filter exceptions that arise when the input is invalid
    try:
        a = input("Please input the lower bound:")
        a = eval(a) # ensuring that a is a number or pi
        break
    except SyntaxError or ValueError:
        print(f"{a} is not a number or pi. Try again...")

while True: # endless loop inserted after requiring input to filter exceptions that arise when the input is invalid
    try:
        b = input("Please input the upper bound:")
        b = eval(b) # ensuring that b is a number or pi
        break
    except SyntaxError or ValueError:
        print(f"{b} is not a number or pi. Try again...")

n = 100000
x = np.random.uniform(a,b,n) # creating range

while True: # endless loop inserted after requiring input to filter exceptions that arise when the input is invalid
    try:
        y = input("Please input the function you wish to integrate:")
        s = eval(y)
        break
    except SyntaxError:
        print(f"{y} is not recognisable as a function. Try again...")
    

def I(x,y): # convert y from string to function
    '''
    The function converts a string to a function.
    Params: x (array) domain, over which y is evaluated.
            y (str) needs to be converted into a function.
    Return: I (func) the function created from y.
    '''
    I = eval(y)
    return I

integral1,error = scipy.integrate.quad(I,a,b,args = (y,))

print(f"The result of the user-supplied integral using the function 'scipy.integrate.quad()': {integral1}")

# using the above method to find the result of the given integral:

a = 0
b = pi

def y(x):
    '''
    The function calculates the values of the given function for a domain.
    Params: x (array) the elements of the domain
    Return: y (array) the values of the function over the domain
    '''
    y = x**4+exp(sin(x)+cos(x))
    return y

integral2,error = scipy.integrate.quad(y,a,b)
print(f"The result of the integral of the given function': {integral2}")

def montecarlo(x,y):
    '''
    The function calculates the integral of a given function.
    Params: x (np.array) elements in the domain of the function
            y (array) the function that needs to be integrated
    Return: integral (float): the integral obtained via the Monte Carlo method
    '''
    integral = (np.max(x)-np.min(x))/len(x)*sum(y(x))
    return integral

print(f"The result of the integral using Monte Carlo's method: {montecarlo(x,y)}")


if abs(montecarlo(x,y)-integral2) <= 0.5: # not equal because monte carlo's is an approximation that is worse in the case of more steeply changing functions
    print("The two results are approximately the same.")
