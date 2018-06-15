# from sklearn.model_selection import train_test_split

def data_shuffle(*Xs, y=None, seed=None):
    idx = np.arange(len(Xs[0]))
    np.random.seed(seed)
    np.random.shuffle(idx)
    return [X[idx] for X in Xs], y[idx]
