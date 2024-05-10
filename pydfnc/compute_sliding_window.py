import numpy as np

def gaussianwindow(N, x0, sigma):
    x = np.arange(N-1)
    w = np.exp(- ((x-x0)**2)/ (2 * sigma * sigma)).T
    return w

def compute_sliding_window(nT, win_alpha, wsize):
    nT1 = nT
    if nT % 2 != 0:
        nT = nT + 1
    m = nT/2
    w = int(np.round(wsize/2))
    gw = gaussianwindow(nT, m, win_alpha)
    b = np.zeros((nT, 1))
    b[int(m -w + 1):int(m+w)] = 1
    print(gw.shape, b.shape)
    c = np.convolve(gw.squeeze(), b.squeeze())
    c = c/max(c)
    c = c[int(m+1):int(len(c)-m+1)]
    c = c[:nT1]
    return c