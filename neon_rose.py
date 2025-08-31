import numpy as np
import matplotlib.pyplot as plt


plt.style.use('dark_background')
o = np.linspace(0, 2 * np.pi, 1000)
r = np.sin(7 * o)

x, y = r * np.cos(o), r * np.sin(o)

plt.scatter(x, y, c=o, cmap="plasma", s=5)

plt.axis('equal'); plt.savefig('neon_rose.png'); plt.show()
