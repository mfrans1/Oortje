import numpy as np
from scipy.ndimage import label

from oortje.spectrogram import Spectrogram


class BirdCall:
    def __init__(self, spectrogram: Spectrogram):
        self.power = spectrogram.power
        self.frequencies = spectrogram.frequencies
        self.times = spectrogram.times

        self.mask = np.isfinite(self.power)  # mask for valid data points

        structure = np.ones((3, 3), dtype=int)

        self.labeled_array, self.num_features = label(
            self.mask,
            structure=structure
        )


    def get_feature_vectors(self):
        pass