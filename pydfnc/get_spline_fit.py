import numpy as np
def get_spline_fit(estimates,seqlen,TR):
    numP = np.floor(seqlen/30)
    t = range(TR, (len-1)*TR)
    # t = t(:);
    x0  = estimates
    yfit = x0[0]*t + x0[1]*t.^2;
    for ii in range(numP):
        yfit = yfit + x0[1+ii] * np.sin(2*np.pi*ii*t/(seqlen*TR)) + x0[1+ii] *np.cos(2*np.pi*ii*t/(seqlen*TR))
    return yfit

