import numpy as np
def despike(tc, TR, c1=2.5, c2=3):
    mx1 = np.ones(tc.size, 1)
    mx2 = (np.arange(-1, 1, 2/tc.size - 1)).T
    modelX = np.concatenate([mx1, mx2], 1)
    lestimates = (modelX.T @ modelX) / (modelX.T @ tc)
    ylfit = lestimates[0] + lestimates[1]@mx2
    # TODO: icatb_myquadfun
    # TODO: icatb_mysplinefun
    