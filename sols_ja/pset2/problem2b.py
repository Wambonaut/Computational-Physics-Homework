import numpy as np
import matplotlib.pyplot as plt
import random as rng
from problem2 import traj3body

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
dt = 0.0001
N = 100000

# Place the origin at the center of mass
X = np.sum([m[i] * x0[i] for i in range(3)], axis=0) / np.sum(m)
x0 -= X

# Compute the trajectories
t, x, xd = traj3body(x0, xd0, m, dt, N)

# Plot trajectories
fig, ax = plt.subplots()
plt.axis('equal')
for i in range(3):
  plt.plot(x[i, :, 0], x[i, :, 1])

# Show plots
plt.show()
