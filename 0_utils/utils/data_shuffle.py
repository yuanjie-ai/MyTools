def data_shuffle(X, y, seed=None):
    idx = np.arange(len(X))
    np.random.seed(seed)
    np.random.shuffle(idx)
    return X[idx], y[idx]
