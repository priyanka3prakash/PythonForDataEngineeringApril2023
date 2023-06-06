import numpy as np
from scipy.io.wavfile import write

# Sample rate (number of samples per second)
sample_rate = 44100

# Duration of the audio in seconds
duration = 5

# Generate a time array
t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)

# Generate a sine wave at 440 Hz (A4 note)
frequency = 440
audio = np.sin(2 * np.pi * frequency * t)

# Scale the audio amplitude to 16-bit signed integer range
audio = (audio * 32767).astype(np.int16)

# Write the audio data to a WAV file
write("example.wav", sample_rate, audio)


# assignment: apply all trigonometric functions of ths audio and generate .wav files
