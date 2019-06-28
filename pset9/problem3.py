import matplotlib.pyplot as plt
import numpy as np
from numpy import pi, sqrt
import os
import random

figFolderPath = os.path.join(
  os.path.dirname(os.path.realpath(__file__)), 'figures'
)
if not os.path.exists(figFolderPath):
  os.makedirs(figFolderPath)

def f(x):
  return sqrt(1 - x**2)

def pi_est(N):
  n_acc = 0
  for _ in range(N):
    x = random.random()
    y = random.random()
    if y <= f(x):
      n_acc += 1

  pi_est = 4 * n_acc / N
  return pi_est

N = np.logspace(1, 6, 50)
pi_ests = np.array([pi_est(int(N_)) for N_ in N])
err = np.array([np.abs(1 - pi_est_ / pi) for pi_est_ in pi_ests])

for pi_est_ in pi_ests:
  print(pi_est_)
print()
print(pi)

plt.xlabel(r'$N$')
plt.ylabel(r'$1 - \pi_\mathrm{est} / \pi$')
plt.loglog(N, err)

plt.savefig(os.path.join(figFolderPath, 'fig3.pdf'),
  bbox_inches='tight', pad_inches=0.6)
plt.savefig(os.path.join(figFolderPath, 'fig3.pgf'),
  bbox_inches='tight')
