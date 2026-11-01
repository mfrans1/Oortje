# this will be responsible for decomposing the spectrogram into something useful

# probobably using classes again

"""
decompositoin idea: 

now we have cleaned spectrograms, ie just valid 
data and nan otherwise. 

now we want to compare different spectrograms of different
birds and group them into different classes. we know
all the recordings are of one unique bird species.

label the calls into differnt features, then for each feature
we can find a vector to describe it:

avg frequency, freq width, duration

all features will have a vector, so a bird will have a matrix
    - can we compare these matrices directly? probably not
    - need to decompose the matrices into something smaller, svd
    - then we can compare the decomposition of the bird matrices with 
      each other? 
    
"""


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