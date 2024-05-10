import os
import matplotlib.pyplot as plt 
import seaborn as sb
import scipy.io as sio
import scipy.signal as ssi
import argparse
import numpy as np
from pydfnc.compute_sliding_window import compute_sliding_window
parser = argparse.ArgumentParser()
parser.add_argument("--data", default="")
args = parser.parse_args()
data = args.data.split(",")
# Load ICA Timecourses
X = sio.loadmat("data/fbirn_tc.mat")["TC"]
print(list(X.shape))

# Detrend
X_detrend = ssi.detrend(X, axis=1, type="linear")

# Regress - ignore

# Resample - ignore

# Despike
TR = 2
NyqF = (1/TR) / 2
Wn = int(0.15 / NyqF)

X = ssi.savgol_filter(X, Wn, 3, axis=1) # window size 51, polynomial order 3
# icatb_despike_tc

# Filtering
# FORNOW - wrap matlab
# icatb_filt_data

bfilter, afilter = ssi.butter(5, Wn)
X = ssi.filtfilt(bfilter, afilter, X)

# Compute Window

wsize=40
minTP = 159
window_alpha = 0.5
A = compute_sliding_window(minTP, window_alpha, wsize)
Nwin = minTP - wsize
print(A)

# Sliding Window Correlation/NMI etc

# Do clustering

    # Exemplars
    # Elbow
    # Full Number of Clusters

# Other post processing

