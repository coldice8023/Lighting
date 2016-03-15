import numpy as np
from lighting_system import LightingSystem


illuminance_transfer_matrix = np.array([[3, 2, 1], [1, 2, 3]])
system = LightingSystem(illuminance_transfer_matrix, np.array([1, 2]), 4)