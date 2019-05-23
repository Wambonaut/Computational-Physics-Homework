import matplotlib.pyplot as plt
import numpy as np
import os
from matplotlib.widgets import Slider
from numerov import numerov

# Specific function k used in the schrödinger equation
k = lambda z, eps: eps - z

# The values for eps
eps = np.array([5.0, 6.0])

# Number of steps N and step size dz
N = 10000
dz = 0.001

# Initial valuess
z0 = 0.0
psi0 = 0.0
psid0 = 1.0

# Plot the solutions of the numerov algorithm and save them
plt.axis([0, 10, -1, 1])
for e in eps:
  k_eps = lambda x: k(x, e)
  z, psi = numerov(z0, psi0, psid0, k_eps, dz, N)
  plt.plot(z, psi)
plt.xlabel(r'$\eta$')
plt.ylabel(r'$\psi(\eta)$')

if not os.path.exists('figures'):
  os.mkdir('figures')
plt.savefig('figures/fig2_1.pgf')
plt.show()
