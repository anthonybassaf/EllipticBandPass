from scipy import signal
import matplotlib.pyplot as plt
import numpy as np


b, a = signal.iirfilter(17, [2*np.pi*15, 2*np.pi*30], rp=3, rs=60,
                        btype='band', analog=True, ftype='ellip')
w, h = signal.freqs(b, a, 1000)
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.semilogx(w / (2*np.pi), 20 * np.log10(np.maximum(abs(h), 1e-5)))
ax.set_title('Elliptic bandpass frequency response')
ax.set_xlabel('Frequency [Hz]')
ax.set_ylabel('Amplitude [dB]')
ax.axis((10, 100, -100, 10))
ax.grid(which='both', axis='both')

plt.show()