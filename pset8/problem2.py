import numpy as np
from scipy.integrate import solve_ivp
from scipy import signal
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
SIGMA=10
b=8/3.0

r=0.5
def x_dot(t,y):
    return -SIGMA*(y[0]-y[1])
def y_dot(t,y):
    return r*y[0]-y[2]-y[0]*y[2]
def z_dot(t,y):
    return y[0]*y[1]-b*y[2]

def fun(t,y):
    return [x_dot(t,y),y_dot(t,y),z_dot(t,y)]

t0=0
t_end=100
"""
for r in [0.5,1.15,1.3456,24.0,28.0]:
    if r<1:
        y0=[0.1,0.1,0.1]
    else:
        y0=[b*(r-1)+0.1, b*(r-1)+0.1, r-1+0.1]
    k = solve_ivp(fun, (t0, t_end), y0, method='RK45', max_step=0.1)
    y=k["y"]
    t=k["t"]
    fig=plt.figure()
    ax=plt.axes(projection='3d')
    ax.plot3D(y[0], y[1], y[2], label="r=%.4f"%r)
    plt.savefig("r=%.4f.pdf"%r)
plt.show()
"""
###(b)
r=27
y0=[b*(r-1)+0.1, b*(r-1)+0.1, r-1+0.1]
k = solve_ivp(fun, (t0, t_end), y0, method='RK45', max_step=0.1)
y=k["y"]
t=k["t"]
#plt.plot(t,y[2])
#plt.show()
minima=signal.argrelmin(y[2])
plt.plot(y[2][minima][3:-1], y[2][minima][4:])
plt.plot(np.linspace(20,50,10),np.linspace(20,50,10))
plt.savefig("zk.pdf")
plt.show()
