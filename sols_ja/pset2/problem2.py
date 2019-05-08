import matplotlib.pyplot as plt
import numpy as np
from numpy import sqrt
from numpy.linalg import norm

# Differential equation for the second derivative
def xdd(x, m):
  return np.array([
    -m[1] * (x[0] - x[1]) / norm(x[0] - x[1])**3 - m[2] * (x[0] - x[2]) / norm(x[0] - x[2])**3,
    -m[2] * (x[1] - x[2]) / norm(x[1] - x[2])**3 - m[0] * (x[1] - x[0]) / norm(x[1] - x[0])**3,
    -m[0] * (x[2] - x[0]) / norm(x[2] - x[0])**3 - m[1] * (x[2] - x[1]) / norm(x[2] - x[1])**3
  ])

# Returns the trajectories (times, points and tangent vectors) for 3 bodies interacting through gravity
# This function works with 3xNx2 arrays (N 2-dim. vectors for 3 bodies)
def traj3body(x0, xd0, m, dt, N):
  t = np.zeros(N)
  x, xd = np.zeros((3, N, 2), dtype=np.ndarray), np.zeros((3, N, 2), dtype=np.ndarray)
  x[:, 0] = x0
  xd[:, 0] = xd0
  for i in range(1, N):
    t[i] = dt * i / (N - 1)

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
