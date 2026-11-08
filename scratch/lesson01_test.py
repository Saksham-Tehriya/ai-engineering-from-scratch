import sys
print(f"Python {sys.version}")

import numpy as np
print(f"NumP {np.__version__}")
b = np.array([1, 2, 3])
print(f"Vector: {b}, dot product with itself: {np.dot(b, b)}")