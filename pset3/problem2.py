import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from numerov import numerov

eps0 = 2.3381074104549486
k = lambda z, eps: eps - z

N = 10000
dz = 0.001
z0 = 0.0
psi0 = 0.0
psid0 = 1.0

k_eps0 = lambda x: k(x, eps0)
z, psi = numerov(z0, psi0, psid0, k_eps0, dz, N)

plt.axis([0, 10, -1, 1])
lines, = plt.plot(z, psi)
plt.subplots_adjust(left=0.1, bottom=0.2)

def epsSlider_onChanged(eps):
  k_eps = lambda x: eps - x
  z, psi = numerov(z0, psi0, psid0, k_eps, dz, N)

  lines.set_data(z, psi)

epsSliderAx = plt.axes([0.1, 0.025, 0.8, 0.05])
epsSlider = Slider(epsSliderAx, 'eps', 0.0, 10.0, valinit=eps0)
epsSlider.on_changed(epsSlider_onChanged)

plt.show()
