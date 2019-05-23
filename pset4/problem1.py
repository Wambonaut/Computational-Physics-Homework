import numpy as np

eps = 1e-6
A = np.array([[eps, 0.5], [0.5, 0.5]], dtype=np.float32)
B = np.array([[0.5, 0.25]], dtype=np.float32)

def gaussJordan(A, B, pivoting=False, dtype=None):
  B = np.transpose(B)
  n = np.size(A, axis=0)
  if n != np.size(A, axis=1) or n != np.size(B, axis=0):
    raise ValueError
  
  M = np.zeros((n, n + np.size(B, axis=1)), dtype=dtype)
  M[:, :n] = A
  M[:, n:] = B
  
  for i in range(n):
    if pivoting:
      iMax = np.argmax(M[i:, i]) + i
      M[[i, iMax]] = M[[iMax, i]]

    M[i] /= M[i][i]
    for j in range(n):
      if i != j:
        M[j] -= M[j, i] * M[i]
  
  return M[:, n:]

S = gaussJordan(A, B, pivoting=False, dtype=np.float32)
print(S)
