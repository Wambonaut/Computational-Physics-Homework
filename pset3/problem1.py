#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 14 23:46:36 2019

@author: wambo
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.special import eval_hermite

def numerov_step(x, dx, y_n, y_nm1, k):
    k_np1=k(x+dx)
    k_n=k(x)
    k_nm1=k(x-dx)
    y_np1=(2*(1-5/12*dx**2*k_n)*y_n-(1+1/12*dx**2*k_nm1)*y_nm1)/(1+1/12*dx**2*k_np1)
    return y_np1


def numerov(x_0, y_0, ym1, k, dx, N):
    """ Numerically solves diff equation of type y''(x)+k(x)y(x)=0. Arguments: x0, y0, y_m1, time step dx, function k(x), number of steps N"""
    y=np.zeros(N+2)
    x=np.linspace(x_0-dx, x_0+dx*N, N+2)
    y[1]=y_0
    y[0]=ym1
    for i in range(2,N+2):
        y[i]=numerov_step(x[i], dx, y[i-1], y[i-2], k)
        print(y[i])
    return x, y

plt.figure(figsize=(7,20))
for n in range(0,9):
    e=n+0.5
    if n%2==1:
        x, y=numerov(0, 0.01, 0, lambda x: (2*e-x**2), 0.001, (n+2)*900)
    else:
        x, y=numerov(0, 1-0.001**2*e, 1, lambda x: (2*e-x**2), 0.001, (n+2)*800)
    y_anal=eval_hermite(n,x)/(2**n*np.math.factorial(n)*np.sqrt(np.pi))**0.5*np.exp(-x**2/2)
    y_anal=y_anal*y[50]/y_anal[50] #norm the analytical solution
    plt.subplot(911+n)
    plt.plot(x,y, label="Numerical Solution")
    plt.plot(x, y_anal, label="Analytical Solution")
plt.legend()
plt.show()
