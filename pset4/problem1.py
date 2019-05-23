import numpy as np
from scipy.linalg import lu_factor, lu_solve
from linsolve import gaussJordan

eps = 1e-6
A = np.array([[eps, 0.5], [0.5, 0.5]], dtype=np.float32)
b = np.array([[0.5, 0.25]], dtype=np.float32)
S = gaussJordan(A, b, pivoting=False, dtype=np.float32)
x = lu_solve(lu_factor(A), b[0])

print(S[0])
print(x)
