import numpy as np
import math 

def entropy_node(y):
    """
    Compute entropy for a single node using stable logarithms.
    """
    # Write code here
    Y = np.array(y)
    value, counts = np.unique(Y,return_counts = True)
    probs = counts/len(Y)
    return -np.sum(probs * np.log2(probs))
    