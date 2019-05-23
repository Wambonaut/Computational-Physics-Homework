import numpy as np

def gaussJordan(A, b, pivoting=False, dtype=None):
  """ Solves mutiple systems of equations A X = B using the gauss-jordan algorithm"""
  B = np.transpose(b)
  n = np.size(A, axis=0)
  m = np.size(A, axis=1)
  if n != m or n != np.size(B, axis=0):
    raise ValueError
  
  M = np.zeros((n, n + np.size(B, axis=1)), dtype=dtype)
  M[:, :m] = A
  M[:, m:] = B
  
  for i in range(n):
    if pivoting:
      iMax = np.argmax(M[i:, i]) + i
      M[[i, iMax]] = M[[iMax, i]]

    M[i] /= M[i][i]
    for j in range(n):
      if i != j:
        M[j] -= M[j, i] * M[i]
  
  return np.transpose(M[:, n:])
