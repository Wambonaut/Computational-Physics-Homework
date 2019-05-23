import matplotlib.pyplot as plt
import numpy as np
import os
from linsolve import gaussJordan
from numpy.linalg import norm
from scipy.linalg import lu_factor, lu_solve

# Solve the equation system for eps=1e-6 using the gauss-jordan algorithm
#   and LU-Decomposition
eps0 = 1e-6
A = np.array([[eps0, 0.5], [0.5, 0.5]], dtype=np.float32)
b = np.array([[0.5, 0.25]], dtype=np.float32)
X1 = gaussJordan(A, b, pivoting=False, dtype=np.float32)
X2 = gaussJordan(A, b, pivoting=True, dtype=np.float32)
x = lu_solve(lu_factor(A), b[0])

# Print the results
print(X1[0])
print(X2[0])
print(x)
print()
print(np.matmul(A, X1[0]))
print(np.matmul(A, X2[0]))
print(np.matmul(A, x))

# Compute relative deviations of the first solution element
#   for different values of eps
Eps = np.logspace(-3, -9, num=1000)
RDev = np.zeros_like(Eps)
for i, eps in enumerate(Eps):
  A = np.array([[eps, 0.5], [0.5, 0.5]], dtype=np.float32)
  b = np.array([[0.5, 0.25]], dtype=np.float32)
  S = gaussJordan(A, b, pivoting=False, dtype=np.float32)
  x = lu_solve(lu_factor(A), b[0])

  RDev[i] = abs(norm(S[0] - x) / norm(x))

# Plot the deviation in dependence of eps
plt.xlabel(r'$\epsilon$')
plt.ylabel(r'$\frac{|\Delta x|}{|x|}$ / \%')
plt.ylim(0, 110)
plt.semilogx(Eps, 100 * RDev)

# Save the figure
if not os.path.exists('figures'):
  os.mkdir('figures')
plt.savefig('figures/fig1_1.pgf')
plt.show()
