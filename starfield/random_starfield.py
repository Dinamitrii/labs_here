import numpy as np
import matplotlib.pyplot as plt


x = np.random.rand(500)*10
y = np.random.rand(500)*10

sizes= np.random.rand(500)*20

colors= np.random.rand(500)
theme = "dark"
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d', xlim=(0,10), ylim=(0,10), zlim=(0,10))

plt.scatter(x,
            y,
            s=sizes,
            c=colors,
            cmap="twilight",
            edgecolors="none",
            alpha=0.8)

plt.axis('off')
plt.show()
