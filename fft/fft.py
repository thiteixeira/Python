#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np


Fs = 2000.0  # sampling rate
Ts = 1.0/Fs  # sampling interval
t = np.arange(0,1,Ts) # time vector
x = np.linspace(0,2*np.pi,2000)
y = [0 for _ in x]
for n in range(0,2000):
    y += np.sin((2*n+1)*(2*np.pi)*(x))/(2*n+1)

n = len(y) # length of the signal
k = np.arange(n)
T = n/Fs
frq = k/T # two sides frequency range
frq = frq[range(int(n/2))] # one side frequency range

Y = np.fft.fft(y)/n # fft computing and normalization
Y = Y[range(int(n/2))]

fig, ax = plt.subplots(2, 1)
ax[0].plot(t,y)
ax[0].set_xlabel('Time')
ax[0].set_ylabel('Amplitude')
ax[1].plot(frq,abs(Y),'r') # plotting the spectrum
ax[1].set_xlabel('Freq (Hz)')
ax[1].set_ylabel('|Y(freq)|')
plt.tight_layout()
plt.show()
