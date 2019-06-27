import matplotlib.pyplot as plt
import numpy as np
import os
from scipy.integrate import solve_ivp

from ev import lda, v

a = np.array([55, 11, 34])
d = np.array([85, 9, 35])
B = np.array([[20, 30, 5], [1, 3, 7], [4, 10, 20]])
C = np.array([[20, 30, 35], [3, 3, 3], [7, 8, 20]])

def PPd(t,y):
  P = y[:3]
  N = y[3:]
  Nd = N * (a - np.dot(B, P))
  Pd = P * (np.dot(C, N) - d)
  return np.concatenate((Pd, Nd))

c = np.array([3, 3, 1, 1, 5, 0.1])
y0 = np.real(np.dot(v, c))

t0 = 0.0
t1 = 0.05
delta_t = (t1 - t0) / 1000
x = solve_ivp(PPd, (0, 0.05), y0, max_step=delta_t)
for i in range(6):
  if i < 3:
    label = '$N_{%i}(t)$' % (i + 1)
  else:
    label = '$P_{%i}(t)$' % (i - 2)
  plt.semilogy(x['t'], x['y'][i], label=label)
plt.legend()

if not os.path.exists('figures'):
  os.mkdir('figures')
plt.savefig('figures/fig1.pgf')

