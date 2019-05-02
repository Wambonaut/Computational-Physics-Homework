import matplotlib.pyplot as plt
import numpy as np

def I(x, a, n):
  return x**n / (x + a)

a = 5
n = np.array([1, 5, 10, 20, 30, 50])
x = np.linspace(0.0, 1.0, 1000)

fig = plt.figure()
fig.subplots_adjust(hspace=0.3, wspace=0.3)
for i in range(len(n)):
  ax = fig.add_subplot(2, 3, i + 1)
  ax.set_title('n = ' + str(n[i]))
  ax.plot(x, I(x, a, n[i]))

plt.show()
