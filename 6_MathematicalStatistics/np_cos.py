import numpy as np


def np_cos(a, b, adjust=False):
    cos = lambda a, b: np.dot(a, b) / np.linalg.norm(a) / np.linalg.norm(b)
    if adjust:
        m = np.array([a, b]).mean()
        return cos(a - m, b - m)
    return cos(a, b)
