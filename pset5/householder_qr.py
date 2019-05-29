import numpy as np
from numpy import sqrt
from numpy.linalg import norm, inv

def _householder_proj(x):
  u = x.copy()
  u[0] -= norm(u)
  return np.identity(np.size(u)) - 2 * np.outer(u, u) / np.inner(u, u)

def householder(A):
  """
  Applys the householder algorithm, which brings the matrix A, via a similarity transformation into a tridiagonal form, if A is symmetric
  and into the Hessenberg form in the general case.
  """

  # Test if A is matrix
  if not A is np.ndarray:
    raise ValueError
  shape = np.shape(A)
  if len(shape) != 2:
    raise ValueError
  n, m = shape
  if n != m:
    raise ValueError

  # Apply householder iterations
  for i in range(n - 2):
    x = A[i+1:,i].copy()
    P = np.identity(n)
    P_sub = _householder_proj(x)
    P[i+1:,i+1:] = P_sub

    A = np.matmul(A, P)
    A = np.matmul(P, A)

  return A

def qr_decomp(A):
  """
  Applys the qr decomposition algorithm, which decomposes a symmetric matrix A into an orthonormal matrix Q and an upper triangular matrix R.
  """

  # Test if A is a symmetric matrix
  if not A is np.ndarray:
    raise ValueError
  shape = np.shape(A)
  if len(shape) != 2:
    raise ValueError
  n, m = shape
  if n != m:
    raise ValueError

  # Apply qr decomposition iterations
  R = A.copy()
  Q = np.identity(n)
  for i in range(n-1):
    x = R[i:,i].copy()
    P = np.identity(n)
    P_sub = _householder_proj(x)
    P[i:,i:] = P_sub

    R = np.matmul(P, R)
    Q = np.matmul(Q, np.transpose(P))

  return Q, R

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
Q, R = qr_decomp(A)

print(np.round(T, decimals=2))
print()
print(np.round(Q, decimals=2))
print(np.round(inv(Q), decimals=2))
print()
print(np.round(R, decimals=2))
print()
print(np.round(np.matmul(Q, R), decimals=2))
