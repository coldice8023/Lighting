import matplotlib.pyplot as plt


def plot_convex_hull(cvx_hull):
	for simplex in cvx_hull.simplices:
		plt.plot(points[simplex, 0], points[simplex, 1], 'k-')
	plt.show()
