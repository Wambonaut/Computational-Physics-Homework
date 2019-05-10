import matplotlib.pyplot as plt
import numpy as np
from numpy import exp

# General implementation of 4th order runge kutta algorithm
# ODE: u'(t) = f(u(t), t) where u(t0) = u0
def rk4(f, t0, u0, dt, N):
  t = np.zeros(N)
  u = np.zeros(N)

  t[0] = t0
  u[0] = u0
  for i in range(1, N):
    k1 = f(t[i - 1], u[i - 1])
    k2 = f(t[i - 1] + dt / 2, u[i - 1] + k1 * dt / 2)
    k3 = f(t[i - 1] + dt / 2, u[i - 1] + k2 * dt / 2)
    k4 = f(t[i - 1] + dt, u[i - 1] + k3 * dt)
    ud = (k1 + 2 * k2 + 2 * k3 + k4) / 6

    t[i] = t[i - 1] + dt
    u[i] = u[i - 1] + ud * dt
  return t, u

# RHS of the ODE
def f(u, r):
  return -r * u

# Analytical solution
def u(t, r):
  return exp(-r * t)

# Arrays for the plot of the analytical solution
t_a = np.linspace(0, 10, 1000)
u_a = u(t_a, 1)

# Plot numerical and analytical solutions normal and logarithmic
fig1, ax1 = plt.subplots()
fig2, ax2 = plt.subplots()

ax1.semilogy(t_a, u_a)
ax2.plot(t_a, u_a)
for N in [5, 6, 7, 10, 12]:
  t, u = rk4(lambda t, u: f(u, 1), 0, 1, 10 / (N - 1), N)
  ax1.semilogy(t, u)
  ax2.plot(t, u)

fig1.savefig('sols_ja/pset2/figures/fig1_1.png', papertype='a4',
  orientation='landscape', bbox_inches='tight', format='png')
fig2.savefig('sols_ja/pset2/figures/fig1_2.png', papertype='a4',
  orientation='landscape', bbox_inches='tight', format='png')

plt.show()
