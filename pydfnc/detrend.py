import numpy as np

def detrend(y, num_DataSets=1, detrendNumber=0):
    # make y into a column vector
    if len(y.shape) == 1 or y.shape[0] != 1:
        y = y.T
    num_DataSets = 1
    result = np.zeros_like(y)
    nTerms = 1
    rowStart = 1
    nColumns = y.shape[1]
    b = np.zeros(nTerms*num_DataSets, nColumns)
    for nColumns in range(y.shape[1]):

    pass