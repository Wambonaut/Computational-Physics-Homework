import numpy as np
import matplotlib.pyplot as plt
import random as rng
from problem2 import traj3body

# Parameters and initial conditions
m = np.array([1, 1, 1])
x0 = np.array([
  [-0.97000436,  0.24308753],
  [ 0.97000436, -0.24308753],
  [ 0.00000000,  0.00000000]
])
xd0 = np.array([
  [-0.46620368, -0.43236573],
  [-0.46620368, -0.43236573],
  [ 0.93240737,  0.86473146]
])
dt = 0.01
N = 1000

# Compute the trajectories
t, x, xd = traj3body(x0, xd0, m, dt, N)

# Plot trajectories
fig, axes = plt.subplots(nrows=3, ncols=1)
for i in range(len(axes)):
  axes[i].axis('equal')
  axes[i].plot(x[i, :, 0], x[i, :, 1], color=('C' + str(i)))

# Show plots
plt.show()
