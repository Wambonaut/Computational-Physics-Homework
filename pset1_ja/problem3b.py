from problem3 import yn

a = float(input('a = '))
yn0 = float(input('yn0 = '))
n0 = int(input('n0 = '))
n1 = int(input('n1 = '))
print()

nVals, yVals = yn(yn0, n0, n1, a)

for n, y in zip(nVals, yVals):
  print(str(n) + ' : ' + '{:0.5f}'.format(y))
