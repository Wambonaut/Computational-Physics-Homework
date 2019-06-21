import matplotlib.pyplot as plt
import numpy as np
import os
from scipy.optimize import root

with open('pset8/zeros.dat') as f:
  lines = f.readlines()

  zeros = np.zeros((len(lines), 3), dtype=complex)
  for i, line in enumerate(lines):
    line = line.replace('*I', 'j')
    zeros_str = np.array(line.split('\t'))
    zeros[i] = zeros_str.astype(complex)

plt.subplots()
plt.xlabel(r'$\mathrm{Re}(\lambda)$')
plt.ylabel(r'$\mathrm{Im}(\lambda)$')
plt.plot(zeros[:,0].real, zeros[:,0].imag)
plt.scatter(zeros[:,0].real, zeros[:,0].imag)
plt.plot(zeros[:,1].real, zeros[:,1].imag)
plt.scatter(zeros[:,1].real, zeros[:,1].imag)
plt.plot(zeros[:,2].real, zeros[:,2].imag)
plt.scatter(zeros[:,2].real, zeros[:,2].imag)

if not os.path.exists('pset8/figures'):
  os.makedirs('pset8/figures')
plt.savefig('pset8/figures/fig2.pgf', bbox_inches='tight', pad_inches=0.0)
