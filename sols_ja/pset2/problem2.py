import matplotlib.pyplot as plt
import numpy as np
import os
from numpy import sqrt, dot
from numpy.linalg import norm

# Not important for the problem, but rather useful for long computation times
def printProgressBar (iteration, total, prefix = '', suffix = '',
  decimals = 1, length = 100, fill = '█'):
    perc = 100 * (iteration / float(total))
    percStr = ("{0:." + str(decimals) + "f}").format(perc)
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('%s |%s| %s%% %s\r' % (prefix, bar, percStr, suffix), end = '')
    # Print New Line on Complete
    if iteration == total: 
        print()

# Differential equation for the second derivative
def xdd(x, m):
  return np.array([
    -m[1] * (x[0] - x[1]) / norm(x[0] - x[1])**3
      - m[2] * (x[0] - x[2]) / norm(x[0] - x[2])**3,
    -m[2] * (x[1] - x[2]) / norm(x[1] - x[2])**3
      - m[0] * (x[1] - x[0]) / norm(x[1] - x[0])**3,
    -m[0] * (x[2] - x[0]) / norm(x[2] - x[0])**3
      - m[1] * (x[2] - x[1]) / norm(x[2] - x[1])**3
  ])

# Returns the trajectories (times, points and tangent vectors)
# for 3 bodies interacting through gravity. This function works
# with 3xNx2 arrays (N 2-dim. vectors for 3 bodies)
def body3traj(x0, xd0, m, dt, N):
  t = np.zeros(N)
  x, xd = np.zeros((3, N, 2)), np.zeros((3, N, 2))
  x[:, 0] = x0
  xd[:, 0] = xd0
  for i in range(1, N):
    printProgressBar(i, N - 1, suffix='Complete', prefix='Progress')

    t[i] = t[i - 1] + dt

    # Runge kutta for the two first order equations for each body
    k1 = xdd(x[:, i - 1], m)
    l1 = xd[:, i - 1]
    k2 = xdd(x[:, i - 1] + l1 * dt / 2, m)
    l2 = xd[:, i - 1] + k2 * dt / 2
    k3 = xdd(x[:, i - 1] + l2 * dt / 2, m)
    l3 = xd[:, i - 1] + k3 * dt / 2
    k4 = xdd(x[:, i - 1] + l3 * dt, m)
    l4 = xd[:, i - 1] + k4 * dt

    x[:, i] = x[:, i - 1] + (l1 + 2 * l2 + 2 * l3 + l4) * dt / 6
    xd[:, i] = xd[:, i - 1] + (k1 + 2 * k2 + 2 * k3 + k4) * dt / 6
  return t, x, xd

# Returns the mutual distances from trajectories as 3xNx2 array
def body3mutDist(x):
  x_next = np.roll(x, -1, axis=0)
  return norm(x_next - x, axis=2)

def body3minDistTimes(r, t, outPath=None):
  tMinDist = np.array([])
  inds = np.array([], dtype=int)
  for i in range(3):
    for j in range(1, len(t) - 1):
      if r[i, j - 1] > r[i, j] and r[i, j] < r[i, j + 1]:
        tMinDist = np.append(tMinDist, t[j])
        inds = np.append(inds, i)
  
  if outPath != None:
    if not os.path.exists(os.path.dirname(outPath)):
      os.makedirs(os.path.dirname(outPath))
    with open(outPath, 'w') as out:
      for i in range(len(inds)):
        print(inds[i], tMinDist[i], sep='  ', file=out)
  return tMinDist

# Returns the total energy from trajectories as 3xNx2 array and masses
def body3totErg(x, xd, m):
  T, V = np.zeros(np.size(x, axis=1)), np.zeros(np.size(x, axis=1))
  for i in range(3):
    for j in range(len(xd[i])):
      T[j] += 0.5 * m[i] * dot(xd[i, j], xd[i, j])
    V += -m[i] * m[i - 2] / norm(x[i - 2] - x[i], axis=1)
    - m[i] * m[i - 1] / norm(x[i - 1] - x[i], axis=1)
  return T + V
