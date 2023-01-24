import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sig

N = 8192  # length of the signal
L = 256  # length of one segment
overlap = 128  # overlap between segments

# generate signal
k = np.arange(N)
x = sig.chirp(k, 0, N, .5)

# compute and plot spectrogram
plt.figure(figsize=(10, 5))
plt.specgram(x, NFFT=L, Fs=2, noverlap=overlap, sides='onesided')
plt.xlabel(r'$n$')
plt.ylabel(r'$\Omega$ / $\pi$')
cb = plt.colorbar()
cb.set_label(r'$|X[\Omega,n]|$ in dB')
plt.autoscale(tight=True)
plt.show()
