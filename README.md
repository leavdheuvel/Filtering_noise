# Filtering_noise
An algorithm that filters noise in recorded audio.

For a hackaton we produced a sensor that records an ecg. An ecg records the electrical signal from your heart to check for different heart conditions. The sensor we based off of this electric circuit (https://swharden.com/blog/2016-08-08-diy-ecg-with-1-op-amp/):
![image](https://user-images.githubusercontent.com/80387555/115850532-3e8be480-a426-11eb-9f69-0976c05bfd23.png)

The idea is that noise is a signal with high frequency and low amplitude, so that should be the indicators for removing signals.
I used the fast Fourier transform to deal with the noise, mostly bases off of this tutorial: https://realpython.com/python-scipy-fft/

The sensor didn't work that well so we couldn't really so any analysis, but some results either way:
![image](https://user-images.githubusercontent.com/80387555/115860821-579a9280-a432-11eb-8372-df8a12b80f3b.png)
![image](https://user-images.githubusercontent.com/80387555/115860867-6719db80-a432-11eb-9d64-d6ddad0a31cf.png)
![image](https://user-images.githubusercontent.com/80387555/115860904-74cf6100-a432-11eb-933d-b4d751e233e7.png)
![image](https://user-images.githubusercontent.com/80387555/115860946-7ef15f80-a432-11eb-980a-e9efa890915f.png)

Because the threshold of when a signal is noise or not has been put in manually, there is still some noise in the last plot. This differs every time.
