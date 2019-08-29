import sympy as sp
from sympy.utilities.lambdify import lambdify, implemented_function
import numpy as np

# Set up SymPy for symbolic differentiation
x = sp.Symbol('x')
y = (x+5)**2
yprime = y.diff(x)
print("First Derivative: " + str(yprime))

# Convert the first derivative of the input function to a lambda
yprime = lambdify(x, yprime)

# Instantiate gradient descent inputs
cur_x = 10
rate = 0.001
precision = 0.000000000000001
prev_step_size = 1
n = 0 # Current iteration
max_n = 25000 # max iterations

# Loop until precision meets threshold
while prev_step_size > precision and n < max_n:
    prev_x = cur_x
    cur_x = cur_x - rate * yprime(prev_x)
    prev_step_size = abs(cur_x - prev_x)
    n += 1

    # print("Iteration:",n,"\nX:",cur_x)
    
print("The local minimum occurs at", cur_x)
