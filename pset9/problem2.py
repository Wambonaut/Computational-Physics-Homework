import matplotlib.pyplot as plt
import numpy as np
import os
import random

figFolderPath = os.path.join(
  os.path.dirname(os.path.realpath(__file__)), 'figures'
)
if not os.path.exists(figFolderPath):
  os.makedirs(figFolderPath)

x_max = 0.5
y_max = 2.0 / x_max
b = 2 / x_max**2
def p(x):
  return b * x

N = 1000000
x_samples = np.zeros(N)
for i in range(N):
  while True:
    x = x_max * random.random()
    y = y_max * random.random()
    if y <= p(x):
      break
  x_samples[i] = x

plt.hist(x_samples, 100, range=(0, x_max))

plt.savefig(os.path.join(figFolderPath, 'fig2.pdf'),
  bbox_inches='tight', pad_inches=0.6)
plt.savefig(os.path.join(figFolderPath, 'fig2.pgf'),
  bbox_inches='tight')
