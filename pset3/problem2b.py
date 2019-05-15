import matplotlib.pyplot as plt
import numpy as np
from numerov import numerov
from numpy import tan, pi
from scipy.optimize import brentq

eps = 1.0
k = lambda z, eps: eps - z

N = 10000
dx = 0.001
z0 = 0.0
psi0 = 0.0
psid0 = 1.0

def psi_limit(eps):
  k_eps = lambda z: k(z, eps)
  psi = numerov(z0, psi0, psid0, k_eps, dx, N)[1]
  return psi[N - 1]

eps1 = brentq(psi_limit, 1.0, 3.0)
eps2 = brentq(psi_limit, 3.0, 5.0)
eps3 = brentq(psi_limit, 5.0, 6.0)

print(eps1)
print(eps2)
print(eps3)
