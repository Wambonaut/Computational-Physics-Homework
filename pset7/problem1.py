import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt
a_i=np.array([55,11,34])
d_i=np.array([85,9,35])
b_ij=np.array([[20,30,5],[1,3,7],[4,10,20]])#.transpose()
c_ij=np.array([[20,30,35],[3,3,3],[7,8,20]])#.transpose()
##The first three elements of the y vector are P_i, the second three are N_i
def pop_dynamics(t,y):
    P_i=y[:3]
    N_i=y[3:]
    dN_dt=N_i*(a_i-b_ij.dot(P_i))
    dP_dt=P_i*(c_ij.dot(N_i)-d_i)
    return np.concatenate((dP_dt,dN_dt))


x=integrate.solve_ivp(pop_dynamics, (0,1), np.array([1.5,1.5,1.5,1.5,1.5,1.5]),max_step=0.01)
for i in range(6):
    plt.plot(x["t"], x["y"][i], label="%i"%i)
#plt.yscale("log")
plt.legend()
plt.show()
