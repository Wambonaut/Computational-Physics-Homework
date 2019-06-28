import matplotlib.pyplot as plt
import numpy as np
import os
import random

from rng import rng

figFolderPath = os.path.join(
  os.path.dirname(os.path.realpath(__file__)), 'figures'
)
if not os.path.exists(figFolderPath):
  os.makedirs(figFolderPath)

a, c, m = 106, 1283, 6075
I0, J0 = 110, 883

rng1 = rng(I0, a, c, m)
rng2 = rng(J0, a, c, m)

N = 100
x = np.array([rng1.next_int() / (m - 1) for i in range(N)])
y = np.array([rng2.next_int() / (m - 1) for i in range(N)])

x_ = np.array([random.random() for i in range(N)])
y_ = np.array([random.random() for i in range(N)])

plt.subplots()
plt.grid(False)
plt.axis('equal')
plt.scatter(x, y)

plt.savefig(os.path.join(figFolderPath, 'fig11.pdf'),
  bbox_inches='tight', pad_inches=0.6)
plt.savefig(os.path.join(figFolderPath, 'fig11.pgf'),
  bbox_inches='tight')

plt.subplots()
plt.grid(False)
plt.axis('equal')
plt.scatter(x_, y_)

plt.savefig(os.path.join(figFolderPath, 'fig12.pdf'),
  bbox_inches='tight', pad_inches=0.6)
plt.savefig(os.path.join(figFolderPath, 'fig12.pgf'),
  bbox_inches='tight')
