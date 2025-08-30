import numpy as np
import matplotlib.pyplot as plt


plt.style.use('dark_background')
o = np.linspace(0, 2 * np.pi, 1600)
r = 1 + 0.3 * np.cos(12 * o)

x, y = r * np.cos(o), r * np.sin(o)
plt.scatter(x, y, c=o, cmap="rainbow", s=4)
plt.axis('equal'); plt.savefig('electric_flower.png'); plt.show()
