import numpy as np

def numerov(t0, u0, ud0, k, dt, N):
  """ Numerically solves the ODE u''(t) + k(t) u(t) = 0 using the numerov algorithm """
  t = np.linspace(0, (N - 1) * dt, N)
  u = np.zeros(N)
  u[0] = u0
  u[1] = u0 + ud0 * dt
  for i in range(2, N):
    u[i] = 2 * (1 - 5 * k(t[i - 1]) * dt**2 / 12) * u[i - 1] - (1 + k(t[i - 2]) * dt**2 / 12) * u[i - 2]
    u[i] /= (1 + k(t[i]) * dt**2 / 12)
  return t, u
