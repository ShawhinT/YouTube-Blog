# Time Series, Signals, & the Fourier Transform
#### An introduction and primer for future posts

In my next three posts, I will introduce and discuss the Fourier and Wavelet
Transforms, which extract information on how a quantity oscillates over time.
These methods have almost endless applications, a few of which I describe
here.

[**Example code**](https://github.com/ShawhinT/YouTube/tree/main/fourierTransform) link
can be found in the “Resources” section below.

* * *

### Time Series

Everyone is undoubtedly familiar with time series, even if you have not heard
the term. A **time series** is simply **a set of values ordered by time**. For
instance, stock index prices are usually depicted as price vs. time plots on
your favorite news network. Another example is a 7-day forecast, which shows
temperature highs over several days. Time series are a natural way to
represent data.

![](https://cdn-images-1.medium.com/max/800/1*KSGfeQYxRbI9tGjpMbu87g.png)NASDAQ index price
over time is a familiar time series. Image captured from Google search of
“NASDAQ”.![](https://cdn-images-1.medium.com/max/800/1*tExj_F1VumxNq2Q8pxay8A.png)Temperature highs and
lows in a 7-day forecast form a time series. Image captured from Google search
of “weather”.

### Signals

Signals are a type of time series. More specifically, **signals** are**time-
varying quantities that represent physical events**. Two fundamental
properties of signals are: amplitude and frequency. The amplitude of a signal
is its magnitude e.g. the loudness of an audio signal. A signal’s frequency
characterizes its oscillation in time e.g. the pitch emitted by a guitar.

![](https://cdn-images-1.medium.com/max/800/1*QaUWu-_TmyO7yTZ1W3ylmA.png)Audio
signal waveform of music. Signal is left part of stereo mix. Image by author.

Implicitly, when going from a continuous signal (an infinite set of
quantities) to a discrete signal (a finite set of quantities) information is
lost. Thus, a discrete signal is often an approximation of a continuous
signal. For example, consider capturing temperature fluctuations in an office
to run an HVAC system. At any moment, the office will have some average
ambient temperature. Suppose a set of thermometers is used to measure this
temperature every hour. This measurement would generate a discrete signal
approximating the true temperature fluctuations in the office. It is
reasonable to suspect that these hourly recordings of temperature would result
in poor air conditioning since temperatures would likely change over time
scales much smaller than an hour. If so, how frequently should the temperature
be measured? This question is answered formally using the Nyquist Theorem.
Which states to capture a continuous signal reliably, the rate at which
information is recorded, called the sampling rate, must be twice the frequency
of the signal of interest. This is why audio is typically sampled at 44,100
Hz, since the upper limit to human hearing is about 20,000 Hz.

In practice, capturing meaningful information from an environment may not be
so simple. Real-world signals are commonly aperiodic, noisy, and influenced by
multiple sources. Extracting useful information from these signals is a
fundamental goal of signal processing.

### The Fourier Transform

![](https://cdn-images-1.medium.com/max/800/1*PTm2p-z-PPV9sb1-WGl9vw.png)A
definition of the Fourier Transform. Other conventions exist which differ by a
prefactor. Image by author.

At the core of signal processing is the **Fourier Transform (FT)**. The FT
**decomposes a function into sines and cosines** i.e. waves. In theory, any
function can be represented in this way, that is, as a sum of (possibly
infinite) sine and cosine functions of different amplitudes and frequencies. A
toy example is given below. The code can be found at the accompanying [GitHub repo](https://github.com/ShawhinT/YouTube/tree/main/fourierTransform).

![](https://cdn-images-1.medium.com/max/800/1*ByM5OCU2NL8alWCdmpPIVQ.png)**Toy
example signal.** Image by author.![](https://cdn-images-1.medium.com/max/800/1*BA6p3ieGJqGiI0yfMUxwCA.png)**Constituent
frequencies of toy example:** In words, the toy signal can be represented as
the sum of 2 sine functions of frequencies 1 and 2 Hz. Image by author.![](https://cdn-images-1.medium.com/max/800/1*MmZwW3k7hBhQhZpE8P__nA.png)**One sided power
spectrum of toy signal:** Two prominent peaks of equal magnitude are present
at f=1 and 2 Hz corresponding to signal decomposition into two sine functions.
Image by author.

#### Applications

The Fourier Transform has countless applications in spectral analysis, solving
differential equations, and A/V production.

**Audio Production**

Equalization (EQ) is an essential part of audio production. The volume of
specified frequency ranges can be turned up or down, which alters how the
audio sounds. A basic use of EQ is removing background noise from an audio
file.

![](https://cdn-images-1.medium.com/max/800/1*QuV0VxtPWkFxuqKqPZdt3g.png)Top
panel shows an audio signal. Bottom panel shows the EQ, which increases or
decreases the gain of frequency ranges. Image by author.

**EEG**

EEG is a technique for recording electrical activity from the brain. Spectral
analysis of EEG is widely used, that is, the examination of a signal via
constituent frequency energies. A widely used convention of frequency bands in
EEG is given below.

![](https://cdn-images-1.medium.com/max/800/1*tlTTrB0Pva3DXh9pzQBTEw.png)Common frequency
bands used in EEG. Image by author.

### Conclusion

Time series and signals are natural ways to organize data. The Fourier
Transform extracts frequency information embedded in data. There are countless
use cases for this approach in fields such as: audio engineering, physics, and
data science. The Fourier Transform is discretized and made computationally
efficient for practical applications via the **Fast-Fourier Transform (FFT)**
algorithm. The FFT will be discussed in my next post.
