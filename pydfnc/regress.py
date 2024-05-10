import numpy as np

def regress(y, X, compute_residual=True):
    rank_X = np.linalg.matrix_rank(X)

    if rank_X < X.shape[1]:
        a = np.linalg.pinv(X)*y
    else:
        a = (X.T@X) / (X.T @ y)
    if compute_residual:
        residual = y - X@a
        denom = np.sqrt(np.sum(np.power(y - np.mean(y), 2)))
        num = np.sqrt(np.sum(np.power(residual, 2)))
        R2 = 1 - (np.power(np.divide(num, denom), 2))
        return a, R2, residual
    return a