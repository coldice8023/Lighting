import numpy as np


class LightingSystem(object):
    def __init__(self, illuminance_transfer_matrix, covariance_matrix, num_points):
        self.num_user, self.num_LED = illuminance_transfer_matrix.shape
        self.illuminance = np.zeros((self.num_user, 1))
        self.dimming = np.zeros((self.num_LED, 1))
        self.observed_illuminance = np.array([])
        self.observed_feedback = np.array([])
        self.illuminance_set = self.feasible_illuminance(illuminance_transfer_matrix, num_points)
        self.acq_func = np.array([])
        self.covariance_matrix = covariance_matrix
        self.est_sat_fun = np.array([])
        self.est_pref_illuminance = np.nan((self.num_user, 1))

    def feasible_illuminance(self, illuminance_transfer_matrix, num_points):
        from scipy.spatial import Delaunay
        max_illuminance = np.sum(illuminance_transfer_matrix, axis=1)
        illuminance_set = np.meshgrid(*[np.linspace(i, j, num_points) for i, j in zip(np.zeros((self.num_user, 1)), max_illuminance)])
        for i in range(self.num_user):
            illuminance_set[i] = illuminance_set[i].reshape((illuminance_set[i].size, 1))
        illuminance_set = np.stack(illuminance_set)
        d = []
        for num in range(2 ** self.num_LED):
            d.append(list(bin(num)[2:].zfill(self.num_LED)))
        d = np.array(d, dtype=float).T
        x = np.dot(illuminance_transfer_matrix, d).T
        hull = Delaunay(x)
        in_hull = hull.find_simplex(illuminance_set) >= 0
        illuminance_set = illuminance_set[in_hull, :]
        return illuminance_set
