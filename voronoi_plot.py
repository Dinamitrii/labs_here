import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Voronoi, voronoi_plot_2d


pnts = np.random.rand(20, 2)

vor = Voronoi(pnts)
voronoi_plot_2d(vor)
plt.show()



