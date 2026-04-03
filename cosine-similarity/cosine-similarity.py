import numpy as np
import math
from numpy.linalg import norm

def cosine_similarity(a, b):
    """
    Compute cosine similarity between two 1D NumPy arrays.
    Returns: float in [-1, 1]
    """
    m = np.dot(a,b)
    n = norm(a) * norm(b)
    
    if norm(a) ==0 or norm(b) == 0:
        return 0
    else:
        return (m/n)
    pass