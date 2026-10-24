import audio
import numpy as np
from scipy.signal import spectrogram
import matplotlib.pyplot as plt

class Spectrogram:
    def __init__(self, audio: audio.Audio):
        """Initialize the Spectrogram object from an Audio object."""
        self.audio = audio

        self.frequencies, self.times, self.power = spectrogram(
            self.audio.data, fs=self.audio.sample_rate
            )

        self.power = 10 * np.log10(self.power + 1e-10)


    def plot(self):
        # Plot.
        plt.figure(figsize=(12, 5))
        plt.pcolormesh(
            self.times,
            self.frequencies,
            self.power,
            shading="auto",
            cmap="magma",
        )
        plt.colorbar(label="Power (dB)")
        plt.xlabel("Time (s)")
        plt.ylabel("Frequency (Hz)")
        plt.tight_layout()
        plt.show()