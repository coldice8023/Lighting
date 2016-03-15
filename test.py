import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import ConvexHull

def in_hull(p, hull):
    """
    Test if points in `p` are in `hull`

    `p` should be a `NxK` coordinates of `N` points in `K` dimensions
    `hull` is either a scipy.spatial.Delaunay object or the `MxK` array of the
    coordinates of `M` points in `K`dimensions for which Delaunay triangulation
    will be computed
    """
    from scipy.spatial import Delaunay
    if not isinstance(hull, Delaunay):
        hull = Delaunay(hull)
    return hull.find_simplex(p) >= 0

illuminance_transfer_matrix = np.array([[3, 2, 1], [1, 2, 3]])
num_user, num_LED = illuminance_transfer_matrix.shape
d = []
for num in range(2 ** num_LED):
	d.append(list(bin(num)[2:].zfill(num_LED)))
d = np.array(d, dtype = float).T
x = np.dot(illuminance_transfer_matrix, d).T
# points = np.random.rand(30, 2)
hull = ConvexHull(x)
plt.plot(x[:, 0], x[:, 1], 'rx', markersize=20, linewidth=20.0)
for simplex in hull.simplices:
	plt.plot(x[simplex, 0], x[simplex, 1], 'k-')


randx = np.random.rand(1000, num_user) * 6
x_in_hull = in_hull(randx, x)
plt.scatter(randx[x_in_hull == True, 0], randx[x_in_hull == True, 1], s=20, c='green', alpha=0.5)
plt.scatter(randx[x_in_hull == False, 0], randx[x_in_hull == False, 1], s=20, c='red', alpha=0.5)


plt.show()

