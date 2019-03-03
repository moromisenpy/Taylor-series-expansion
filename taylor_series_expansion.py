#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 00:15:23 2019

@author: moromi_senpy
"""
#############################################################
#               Tayler series expansion
#############################################################

#============================================================
#                     Import modules
#============================================================
import numpy as np
import matplotlib.pyplot as plt
import math
#============================================================
#                Definition of Function
#============================================================

## central difference
#def central_difference(x, delta_x):
#	return (f(x + delta_x) - f(x - delta_x)) / (2 * delta_x)

# f(x) = sin(x)
def f(x):
    return np.sin(x)

# hight-order differential (recursive call)
def fn(x,n,delta_x=1e-2):
    if n==0:
        return f(x)
    else:
        return (fn(x+delta_x, n-1, delta_x) - fn(x-delta_x, n-1, delta_x)) / (2*delta_x)
    
#============================================================
#                     Main Routine
#============================================================

x = np.linspace(-5, 5, num=100)
f_hat = np.zeros_like(x)
N = 7 # order
a = np.empty([N+1], dtype=np.float64) # coefficient

# calculate coefficients
for n in range(N+1):
    a[n] = fn(0,n) / math.factorial(n)

# draw function
fig = plt.figure()
plt.plot(x, f(x), linewidth=4, color="red", label="$\sin x$")
for n in range(N+1):
    f_hat = f_hat + a[n]*np.power(x,n)
    plt.plot(x, f_hat, linestyle="dashed", label=r"$\sum_{n=0}^{%d} \frac{f^{(n)}(0)}{n!} x^{n}$" %(n))
    
plt.title("Taylor series expansion")
plt.xlabel("$x$")
plt.xlim([-4,4])
plt.ylim([-1.5,1.5])
plt.grid(True)
plt.legend()
fig.tight_layout()


    