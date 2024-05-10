import numpy as np
def get_quad_fit(estimates,seqlen,TR):
    #%TR = 2;
    numP = np.floor(seqlen/30)
    t = range(TR, (seqlen-1)*TR)
    #t = t[:]
    x0  = estimates
    yfit = x0[0]*np.pow(t,2) + x0[1]*t + x0[2]
    return yfit