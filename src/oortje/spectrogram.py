from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import spectrogram
from scipy.ndimage import label, find_objects, binary_opening, binary_closing

import oortje.audio as audio


class Spectrogram:
    def __init__(self, audio: audio.Audio):
        """Initialize the Spectrogram object from an Audio object."""
        
        self.audio = audio

        self.frequencies, self.times, self.power = spectrogram(
            self.audio.data, fs=self.audio.sample_rate
            )

        self.power = 10 * np.log10(self.power + 1e-10)

        self.max_power, self.min_power = self.power.max(), self.power.min()

    def normalize(self):
        """Normalize the power values to the range [0, 1]."""
        self.power = (self.power - self.min_power) / (self.max_power - self.min_power)

    def denormalize(self):
        """Denormalize the power values back to the original scale."""
        self.power = self.power * (self.max_power - self.min_power) + self.min_power

    def detect_calls(self, threshold: float = 0.5, min_area_bins: int = 10):
        """ Detect active frequency-time bins and update self.calls as a 2D boolean mask. """

        binary_mask = self.power > threshold
        
        structure = [[0, 1, 0], [1, 1, 1], [0, 1, 0]]
        binary_mask = binary_closing(binary_mask, structure=structure)
        binary_mask = binary_opening(binary_mask, structure=structure)
        
        labeled_mask, num_features = label(binary_mask)
        slices = find_objects(labeled_mask)
        
        valid_calls_mask = np.zeros_like(self.power, dtype=bool)
        
        for i, slc in enumerate(slices):
            if slc is None:
                continue
                
            area = np.sum(labeled_mask[slc] == (i + 1))
            if area >= min_area_bins:
                valid_calls_mask[slc] |= (labeled_mask[slc] == (i + 1))
                
        self.calls = valid_calls_mask
        return self.calls

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