import matplotlib.pyplot as plt
import numpy as np
from numpy import sqrt
from numpy.linalg import norm

def xdd1(x1, x2):
  return (x2 - x1) / norm(x2 - x1)**3
def xdd2(x1, x2):
  return (x1 - x2) / norm(x1 - x2)**3

def traj2body(x10, xd10, x20, xd20, dt, N):
  t = np.zeros(N)
  x1, xd1 = np.zeros(N, dtype=np.ndarray), np.zeros(N, dtype=np.ndarray)
  x2, xd2 = np.zeros(N, dtype=np.ndarray), np.zeros(N, dtype=np.ndarray)
  x1[0], xd1[0] = x10, xd10
  x2[0], xd2[0] = x20, xd20
  for i in range(1, N):
    t[i] = dt * i / (N - 1)
    x1[i] = x1[i - 1] + xd1[i - 1] * dt
    x2[i] = x2[i - 1] + xd2[i - 1] * dt
    xd1[i] = xd1[i - 1] + xdd1(x1[i - 1], x2[i - 1]) * dt
    xd2[i] = xd2[i - 1] + xdd2(x1[i - 1], x2[i - 1]) * dt
  return t, x1, x2, xd1, xd2

v0 = 1 / sqrt(2)
x10, v10 = np.array([0.5, 0]), np.array([0, v0])
x20, v20 = np.array([-0.5, 0]), np.array([0, -v0])

t, x1, x2, v1, v2 = traj2body(x10, v10, x20, v20, 0.0001, 40000)

x1 = np.array(x1.tolist())
x2 = np.array(x2.tolist())

fig, ax = plt.subplots()
plt.plot(x1[:,0], x1[:,1])
plt.plot(x2[:,0], x2[:,1])

plt.show()
