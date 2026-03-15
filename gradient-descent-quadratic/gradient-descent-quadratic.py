import numpy as np
def gradient_descent_quadratic(a, b, c, x0, lr, steps):
    """
    Return final x after 'steps' iterations.
    """
    # Write code here
    x = np.array([x0])
    for i in range(steps):
        x = np.append(x, x[i] - lr*(2*a*x[i] + b))
    return x[-1]
    pass