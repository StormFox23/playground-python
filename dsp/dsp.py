from numpy import fft

Nf = 64 # N- DFT size
fs = 64 # sampling frequency
f = 10 # one signal
t = arange(0,1,1/fs) # time-domain samples
deltaf = 1/2. # second nearby frequency
# keep x and y-axes on same respective scale
fig,ax = subplots(2,1,sharex=True,sharey=True)
fig.set_size_inches((8,3))

x=cos(2*pi*f*t) + cos(2*pi*(f+2)*t) # 2 Hz frequency difference
X = fft.fft(x,Nf)/sqrt(Nf)
ax[0].plot(linspace(0,fs,Nf),abs(X),'-o')
ax[0].set_title(r'$\delta f = 2$ Hz, $T=1$ s',fontsize=18)
ax[0].set_ylabel(r'$|X(f)|$',fontsize=18)
ax[0].grid()
x=cos(2*pi*f*t) + cos(2*pi*(f+deltaf)*t) # delta_f frequency difference
X = fft.fft(x,Nf)/sqrt(Nf)
ax[1].plot(linspace(0,fs,Nf),abs(X),'-o')
ax[1].set_title(r'$\delta f = 1/2$ Hz, $T=1$ s',fontsize=14)
ax[1].set_ylabel(r'$|X(f)|$',fontsize=18)
ax[1].set_xlabel('Frequency (Hz)',fontsize=18)
ax[1].set_xlim(xmax = fs/2)
ax[1].set_ylim(ymax=6)
ax[1].grid()