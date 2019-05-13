def I(x, a, n):
  return x**n / (x + a)

def yn(yn0, n0, n1, a):
  rev = n0 > n1
  nRange = list(range(n0, n1, -1 if rev else 1))

  y = yn0
  nVals = [n0]
  yVals = [y]
  for n in nRange:
    if rev:
      y = (1 / n - y) / a
      nVals.append(n - 1)
    else:
      y = 1 / (n + 1) - a * y
      nVals.append(n + 1)
    yVals.append(y)
  return nVals, yVals
