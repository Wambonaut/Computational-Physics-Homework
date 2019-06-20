import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import RK45
SIGMA=10
b=8/3.0

def x_dot(t,y):
    return -SIGMA*(y[0]-y[1])
def y_dot(t,y):
    return r*y[0]-y[2]-y[0]*y[2]
def z_dot(t,y):
    return y[0]*y[1]-b*y[2]

def fun(t,y):
    return [x_dot(t,y),y_dot(t,y),z_dot(t,y)]

y0=[0,0,0]
t0=0
t_end=50
t, y = RK45(fun, t0,y0, t_end)

plt.plot(t,y[0])
plt.plot(t,y[1])
plt.plot(t,y[2])
plt.show()
