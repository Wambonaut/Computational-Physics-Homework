import matplotlib.pyplot as plt
import numpy as np
import os

sigma = 10
b = 8 / 3

def P(x, r):
  return x**3 + (1 + b + sigma) * x**2 + b * (sigma + r) * x + 2 * sigma * b * (r - 1)

r_vals = np.linspace(0.0, 1.8, 4)

plt.subplots()
plt.xlabel(r'$\lambda$')
plt.ylabel(r'$P(\lambda)$')
for r in r_vals:
  x = np.linspace(-13, 5, 1000)
  plt.plot(x, P(x, r))

if not os.path.exists('pset8/figures'):
  os.makedirs('pset8/figures')
plt.savefig('pset8/figures/fig1.pgf', bbox_inches='tight', pad_inches=0.0)
