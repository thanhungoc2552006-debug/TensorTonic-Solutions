import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    # Write code here
    X = np.array(x)
    P = np.array(p)
    if np.sum(P) != 1:
        raise ValueError("Probabilities must sum to 1")
    else:
        return np.dot(X,P)
    pass
