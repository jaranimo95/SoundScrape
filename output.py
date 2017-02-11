import pyaudio
import numpy as np

freqs = {1000, 600, 800, 1200, 350}

p = pyaudio.PyAudio()
for f in freqs:                 # for each sine frequency, in Hz (float)
    volume = 0.5                # amplitude [0.0, 1.0]
    fs = 44100                  # sampling rate, Hz, must be integer
    duration = 2.0/len(freqs)   # in seconds, may be float

    # generate samples, note conversion to float32 array
    samples = (np.sin(2*np.pi*np.arange(fs*duration)*f/fs)).astype(np.float32)
    # for paFloat32 sample values must be in range [-1.0, 1.0]
    stream = p.open(format=pyaudio.paFloat32,
                    channels=1,
                    rate=fs,
                    output=True)

    # play. May repeat with different volume values (if done interactively)
    stream.write(volume*samples)

        # testshit()

stream.stop_stream()
stream.close()

p.terminate()
