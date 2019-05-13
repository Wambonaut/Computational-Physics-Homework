from numpy import log
from problem3 import yn

a = 5
yn0 = log((1 + a) / a)
n0 = 0
n1 = 30
print()

nVals, yVals = yn(yn0, n0, n1, a)

for n, y in zip(nVals, yVals):
  print(str(n) + ' : ' + '{:0.5f}'.format(y))
