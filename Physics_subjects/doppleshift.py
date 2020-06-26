import matplotlib.pyplot as plt
import numpy as np
import wave
import sys
from scipy import absolute
from scipy import signal

def fft_plot(signal_,samplerate,t):
    FTfreq = np.fft.fftfreq(len(signal_),d=1./samplerate)
    FT = np.fft.fft(signal_)
    aFT = absolute(FT)

    fig = plt.figure()
    ax1 = fig.add_subplot(211)
    ax1.plot(t,signal_)
    plt.title('signal_')

    ax2 = fig.add_subplot(212)
    ax2.plot(FTfreq[:int(len(FTfreq)/2)], aFT[:int(len(FTfreq)/2)])
    plt.title('FourierTransform')
    plt.show()



def spectrogram(signal_, samplingrate):
    f, t, Sxx = signal.spectrogram(signal_, samplingrate)
    plt.pcolormesh(t, f, Sxx)
    plt.ylabel('Frequency [Hz]')
    plt.xlabel('Time [sec]')
    plt.show()


def plotting_mixer():
    f1 = 700
    f2 = 300
    samplerate = 4e4
    t = np.arange(0,5,1./samplerate)
    # print(t)
    s1 = np.sin(2*np.pi*f1*t)
    s2 = np.sin(2*np.pi*f2*t)
    s = s1*s2
    # fft_plot(s,samplerate,t)
    spectrogram(s,samplerate)


c = 3e+8
# spf = wave.open("demosample.wav", "r")
# spf = wave.open("cw_radar.wav", "r") #not working
# spf = wave.open("sample1.wav", "r")
spf = wave.open("sample4-optional-but-fun.wav", "r")
samplerate = 1e+8
# Extract Raw Audio from Wav File
signal_ = spf.readframes(-1)
signal_ = np.fromstring(signal_, "Int16")
n = len(signal_)
t = np.linspace(0,5,n)

# If Stereo
if spf.getnchannels() == 2:
    print("Just mono files")
    sys.exit(0)




# fft_plot(signal_,samplerate,t)

plotting_mixer()


def doppler(f_0,f_1):
    """
    f_0 = emitted signal
    f_1 = received signal
    """
    v = -c*(f_0 -f_1)/f_0
    return v
