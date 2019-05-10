import numpy as np
import matplotlib.pyplot as plt
import os
import random as rng
from numpy import abs, log10
from problem2 import body3traj, body3mutDist, body3minDistTimes, body3totErg

# Parameters and initial conditions
m = np.array([3.0, 4.0, 5.0])
x0 = np.array([
  [0.0, 0.0],
  [-4.0, 0.0],
  [-4.0, 3.0]
])
xd0 = np.array([
  [0.0, 0.0],
  [0.0, 0.0],
  [0.0, 0.0]
])

# Place the origin at the center of mass
X = np.sum([m[i] * x0[i] for i in range(3)], axis=0) / np.sum(m)
x0 -= X

# Check for out path
if not os.path.exists('sols_ja/pset2/figures'):
  os.makedirs('sols_ja/pset2/figures')

for N in [100, 10000, 100000, 1000000]:
  dt = 10.0 / N
  n = int(log10(N)) - 1
  minDistTimesPath = 'sols_ja/pset2/out/minDistTimes_' + str(n) + '.txt'

  # Compute the trajectories, mutual distances and total energy
  t, x, xd = body3traj(x0, xd0, m, dt, N)
  r = body3mutDist(x)
  tMinDist = body3minDistTimes(r, t, outPath=minDistTimesPath)
  E = body3totErg(x, xd, m)

  # Plot trajectories
  fig1, ax1 = plt.subplots()
  plt.axis('equal')
  plt.axis([-10, 10, -10, 10])
  for i in range(3):
    plt.plot(x[i, :, 0], x[i, :, 1])

  fig2, ax2 = plt.subplots()
  for i in range(3):
    plt.semilogy(t, r[i])

  fig3, ax3 = plt.subplots()
  plt.semilogy(t, abs(1 - E / E[0]))

  fig1.savefig('sols_ja/pset2/figures/fig2b_' + str(3 * n - 2) + '.png',
    papertype='a4', orientation='landscape', bbox_inches='tight', format='png')
  fig2.savefig('sols_ja/pset2/figures/fig2b_' + str(3 * n - 1) + '.png',
    papertype='a4', orientation='landscape', bbox_inches='tight', format='png')
  fig3.savefig('sols_ja/pset2/figures/fig2b_' + str(3 * n) + '.png',
    papertype='a4', orientation='landscape', bbox_inches='tight', format='png')

plt.show()
