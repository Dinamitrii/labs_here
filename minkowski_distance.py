import numpy as np
from scipy.spatial import distance

# Example points
point_a = [2, 3]
point_b = [5, 7]

# Different parameter values
p_values = [1, 2, 3, 10, np.inf]
print("Minkowski distances using SciPy:")

for p in p_values:
    if np.isinf(p):
        # For p = infinity, use Chebyshev distance
        dist = distance.chebyshev(point_a, point_b)
        print(f"p = ∞, Distance = {dist:.6f} this is Chebyshev distance")
    else:
        dist = distance.minkowski(point_a, point_b, p)
        print(f"p = {p}, Distance = {dist:.6f} this is Minkowski distance")
