# Filtering_noise
An algorithm that filters noise in recorded audio.

For a hackaton we produced a sensor that records an ecg. An ecg records the electrical signal from your heart to check for different heart conditions. The sensor we based off of this electric circuit (https://swharden.com/blog/2016-08-08-diy-ecg-with-1-op-amp/):
![image](https://user-images.githubusercontent.com/80387555/115850532-3e8be480-a426-11eb-9f69-0976c05bfd23.png)

The idea is that noise is a signal with high frequency and low amplitude, so that should be the indicators for removing signals.
I used the fast Fourier transform to deal with the noise, mostly bases off of this tutorial: https://realpython.com/python-scipy-fft/

The sensor didn't work that well so we couldn't really so any analysis, but I did record audio using my laptop's mic. Some results:
![image](https://user-images.githubusercontent.com/80387555/115857296-cde8c600-a42d-11eb-9e43-b0fbb4652781.png)
![image](https://user-images.githubusercontent.com/80387555/115857326-d93bf180-a42d-11eb-8180-5cd0f79fd565.png)
![image](https://user-images.githubusercontent.com/80387555/115857358-e22cc300-a42d-11eb-8261-872e4a746cfb.png)
![image](https://user-images.githubusercontent.com/80387555/115857375-e9ec6780-a42d-11eb-842b-5ff055789268.png)
