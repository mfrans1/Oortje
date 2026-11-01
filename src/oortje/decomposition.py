import numpy as np
from oortje.spectrogram import Spectrogram
from oortje.audio import Audio
from scipy.ndimage import label
import matplotlib.pyplot as plt

class BirdCall:
    def __init__(self, spectrogram: Spectrogram):
        self.power, self.frequencies, self.times = spectrogram.power, spectrogram.frequencies, spectrogram.times

        self.mask = np.isfinite(self.power)  # mask for valid data points

        structure = np.ones((3, 3), dtype=int)

        self.labeled_array, self.num_features = label(
            self.mask,
            structure=structure
        )


    def get_feature_vectors(self):
        pass