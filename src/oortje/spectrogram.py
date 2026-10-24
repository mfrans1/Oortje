import Path
import oortje.audio as audio
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


    def plot(self, save: bool = False, save_path: str = "output/spectrogram.png"):
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

        if save and Path(save_path).parent.exists():
            plt.savefig(save_path)
        elif save and not Path(save_path).parent.exists():
            raise FileNotFoundError(
                f"Directory does not exist: {Path(save_path).parent}"
                )

        plt.show()