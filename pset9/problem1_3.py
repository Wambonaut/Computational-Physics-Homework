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
I0 = 329

r = rng(I0, a, c, m)

N = 10000
n = np.zeros(N)
for i in range(N):
  n[i] = np.sum([(r.next_int() % 6) + 1 for i in range(10)])

plt.hist(n, bins=50)

plt.savefig(os.path.join(figFolderPath, 'fig15.pdf'),
  bbox_inches='tight', pad_inches=0.6)
plt.savefig(os.path.join(figFolderPath, 'fig15.pgf'),
  bbox_inches='tight')
