import matplotlib.pyplot as plt
import numpy as np
from numerov import numerov
from numpy import tan, pi
from scipy.optimize import brentq

def psi_limit(eps):
  """ Returns the last value of the solution psi """
  k_eps = lambda z: k(z, eps)
  psi = numerov(z0, psi0, psid0, k_eps, dz, N)[1]
  return psi[N - 1]

# Specific function k for the schrödinger equation
k = lambda z, eps: eps - z

# Number of steps N and step size dz
N = 10000
dz = 0.001

# Initial values
z0 = 0.0
psi0 = 0.0
psid0 = 1.0

# Calculate the eigenvalues
eps = np.zeros(3)
bounds = np.array([[1.0, 3.0], [3.0, 5.0], [5.0, 6.0]])
for i in range(len(eps)):
  eps[i] = brentq(psi_limit, *bounds[i])
  print(eps[i])
