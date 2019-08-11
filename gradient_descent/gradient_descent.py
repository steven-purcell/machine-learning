import sympy as sp
from sympy.utilities.lambdify import lambdify, implemented_function
import numpy as np

x = sp.Symbol('x')
y = (x+5)**2
yprime = y.diff(x)
yprime = lambdify(x, yprime)

cur_x = 10
rate = 0.001
precision = 0.000000000000001
prev_step_size = 1
iters = 0
max_iters = 25000

df = yprime

while prev_step_size > precision and iters < max_iters:
    prev_x = cur_x
    cur_x = cur_x - rate * df(prev_x)
    prev_step_size = abs(cur_x - prev_x)
    iters += 1

    print("Iteration",iters,"\nX value is",cur_x)
    
print("The local minimum occurs at", cur_x)
