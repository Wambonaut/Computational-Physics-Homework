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
I0 = 110

r = rng(I0, a, c, m)

N = 100
I = np.array([r.next_int() / (m - 1) for i in range(N)])
I_ = np.array([random.random() for i in range(N)])

plt.subplots()
plt.grid(False)
plt.axis('equal')
plt.xlabel(r'$I_j$')
plt.ylabel(r'$I_{j+1}$')
plt.scatter(I[:-1], I[1:])

plt.savefig(os.path.join(figFolderPath, 'fig13.pdf'),
  bbox_inches='tight', pad_inches=0.6)
plt.savefig(os.path.join(figFolderPath, 'fig13.pgf'),
  bbox_inches='tight')

plt.subplots()
plt.grid(False)
plt.axis('equal')
plt.xlabel(r'$I_j$')
plt.ylabel(r'$I_{j+1}$')
plt.scatter(I_[:-1], I_[1:])

plt.savefig(os.path.join(figFolderPath, 'fig14.pdf'),
  bbox_inches='tight', pad_inches=0.6)
plt.savefig(os.path.join(figFolderPath, 'fig14.pgf'),
  bbox_inches='tight')
