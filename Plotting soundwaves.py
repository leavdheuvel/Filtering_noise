# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 07:14:57 2021

@author: Gebruiker
"""

import pyaudio
import numpy as np
import matplotlib.pyplot as plt

#%% Record data
CHUNK = 4096 # Number of data points to read at a time
RATE = 44100 # Time resolution of the recording device (Hz)
DURATION = CHUNK/RATE # Seconds 

p=pyaudio.PyAudio() # Start the PyAudio class
stream=p.open(format=pyaudio.paInt16,channels=1,rate=RATE,input=True,
              frames_per_buffer=CHUNK) # Uses default input device
x_axis = range(CHUNK)

plt.rcParams['figure.figsize'] = (20, 10)

# Create a numpy array holding a single read of audio data
#for i in range(10): #to it a few times just to see
data = np.fromstring(stream.read(CHUNK),dtype=np.int16)
print(data)
plt.plot(x_axis, data)
plt.title("Original data")
plt.show()

# Close the stream gracefully
stream.stop_stream()
stream.close()
p.terminate()

#%% Cleaning the data, removing the noise

from scipy.fft import fft, fftfreq

# Number of samples in normalized_tone
N = RATE * DURATION

yf = fft(data)
xf = fftfreq(int(N), 1 / RATE)

plt.plot(xf, np.abs(yf))
plt.show()

#%%
from scipy.fft import rfft, rfftfreq

# Note the extra 'r' at the front
yf = rfft(data)
xf = rfftfreq(int(N), 1 / RATE)

plt.plot(xf, np.abs(yf))
plt.title("Fourier transform")
plt.show()

#%%
# The maximum frequency is half the sample rate
points_per_freq = len(xf) / (RATE / 2)

# Our target frequency is 4000 Hz
target_idx = int(points_per_freq * 4000)

yf[target_idx-250 : int(max(xf))] = 0

plt.plot(xf, np.abs(yf))
plt.title("High frequency and low amplitude removed")
plt.show()

#%% Invert the data
from scipy.fft import irfft

new_sig = irfft(yf)

plt.plot(x_axis, new_sig)
plt.title("Noise removed")
plt.show()













