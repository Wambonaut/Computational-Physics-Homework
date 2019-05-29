import numpy as np
from numpy.linalg import norm

def householder(A):
  """
  Applys the householder algorithm, which brings the matrix A, via a similarity transformation into a tridiagonal form, if A is symmetric
  and into the Hessenberg form in the general case.
  """

  shape = np.shape(A)
  if len(shape) != 2:
    raise ValueError
  n, m = shape
  if n != m:
    raise ValueError

  for i in range(n - 2):
    u = A[i+1:,i].copy()
    u[0] -= norm(u)
    P_sub = np.identity(n - i - 1) - 2 * np.outer(u, u) / np.inner(u, u)
    P = np.identity(n)
    P[i+1:,i+1:] = P_sub
    A = np.matmul(A, P)
    A = np.matmul(P, A)

  return A

# Example/Test
A = np.array([
  [ 1.0, -3.0,  5.0,  5.0, -3.0,  4.0],
  [-3.0,  5.0,  2.0,  2.0, -6.0,  5.0],
  [ 5.0,  2.0, -9.0,  2.0, -1.0,  2.0],
  [ 5.0,  2.0,  2.0,  7.0,  2.0,  9.0],
  [-3.0, -6.0, -1.0,  2.0, -6.0, -5.0],
  [ 4.0,  5.0,  2.0,  9.0, -5.0,  3.0]
])

T = householder(A)
