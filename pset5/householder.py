import numpy as np
from numpy.linalg import norm

def householder(A):
  u = A[:,0]
  u[0] += norm(u)
  H = 0.5 * np.inner(u, u)

  p = np.matmul(A, u) / H
  K = 0.5 * np.inner(u, p) / H

  U = np.outer(p - K * u, u)
  A = A - U - np.transpose(U)
  return A

A = np.array([
  [ 1.0, -3.0,  5.0],
  [-3.0,  5.0,  2.0],
  [ 5.0,  2.0, -9.0]
])

T = householder(A)

print(T)
