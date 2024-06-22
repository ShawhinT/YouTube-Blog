# CODE AUTHORED BY: SHAWHIN TALEBI

"""
    FUNCTION TO SMOOTH SIGNAL VIA WAVELET DECOMPOSITION

    INPUTS:
    - y = array-like signal to smooth

    OUTPUTS:
    - y_rec = smoothed version of input signal

    DEPENDENCIES:
    - PyWavelets 1.3.0
    - numpy 1.21.5
"""

import pywt
import numpy as np

def smooth_with_wavelets(y):

    # wavelet decomposition
    coeffs = pywt.wavedec(y, 'sym5', mode='symmetric')

    # zero out last 5 detail coefficents
    for i in range(5):
        coeffs[i+5] = np.zeros(coeffs[i+5].shape)

    # wavelet recomposition
    y_rec = pywt.waverec(coeffs, 'sym5', mode='symmetric')[1:]

    return y_rec
