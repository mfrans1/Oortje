import audio
from scipy.signal import spectrogram

class Spectrogram:
    def __init__(self, audio: audio.Audio):
        self.audio = audio
        