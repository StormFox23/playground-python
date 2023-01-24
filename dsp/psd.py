import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
import os

# read audio file 
path = os.path.dirname(os.path.abspath(__file__))
fs, x = wavfile.read(path + '\data\speech_8k.wav')
x = np.asarray(x, dtype=float)
N = len(x)

# compute ACF
acf = 1 / len(x) * np.correlate(x, x, mode='full')
# compute PSD
psd = np.fft.fft(acf)
psd = psd * np.exp(1j * np.arange(2 * N - 1) * 2 * np.pi * (N - 1) / (2 * N - 1))
f = np.fft.fftfreq(2 * N - 1, d=1 / fs)

# plot PSD
plt.figure(figsize=(10, 8))
plt.plot(f, np.real(psd))
plt.title('Estimated power spectral density')
plt.ylabel(r'$\hat{\Phi}_{xx}(e^{j \Omega})$')
plt.xlabel(r'$f$')
plt.axis([0, 2000, 0, 1.1 * max(np.abs(psd))])
plt.grid()
plt.show()
