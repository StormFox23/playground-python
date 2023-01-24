import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt

b, a = signal.iirdesign(wp=100, ws=200, gpass=2.0, gstop=40., analog=True)
w, h = signal.freqs(b, a)

plt.title('Analog filter frequency response')
plt.plot(w, 20 * np.log10(np.abs(h)))
plt.ylabel('Amplitude Response [dB]')
plt.xlabel('Frequency')
plt.grid()
plt.show()
