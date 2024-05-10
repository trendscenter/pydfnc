"""
Custom detrending
"""

import numpy as np
from pydfnc.regress import regress

def detrend(y, num_DataSets=1, detrendNumber=0, diffTimepoints=None):
    # make y into a column vector
    if len(y.shape) == 1 or y.shape[0] != 1:
        y = y.T
    nPoints = y.shape[0]
    num_DataSets = 1
    if diffTimepoints is None:
        numTimepoints = np.ceil(nPoints / num_DataSets).astype(int)
        numTimepoints = np.matlib.repmat(numTimepoints, 1, num_DataSets)
    else:
        if len(diffTimepoints) != num_DataSets:
            raise(ValueError("length of different time points must be the same as the number of data sets"))
        numTimepoints = diffTimepoints
    
    if np.prod(numTimepoints.shape) != len(numTimepoints):
        raise ValueError("different time points must be a vector")

    removeTrend = np.zeros_like(y)
    
    if detrendNumber == 0:
        nTerms = 1
        rowStart = 1
        nColumns = y.shape[1]
        b = np.zeros(nTerms*num_DataSets, y.shape[1])
        for nDatasets in range(num_DataSets):
            rowEnd = np.sum(numTimepoints[:num_DataSets])
            X = np.ones((numTimepoints[nDatasets], 1))
            for nColumns in range(y.shape[1]):
                idx = list(range(nTerms))
                b[nTerms*(nDatasets - 1) + idx] = regress(y[rowStart:rowEnd, nColumns], X)
                removeTrend[rowStart:rowEnd, nColumns] = X@b[nTerms*(nDatasets - 1) + idx, nColumns]
            rowStart = rowEnd + 1
    return y - removeTrend