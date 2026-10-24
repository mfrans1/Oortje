from oortje.spectrogram import Spectrogram
from oortje.audio import Audio

def test_spectrogram_initialization():
    # Test with a valid Audio object
    audio = Audio("data/wav/01 Eastern Backyard Birds.wav")
    spectrogram = Spectrogram(audio)
    
    assert spectrogram.audio == audio
    assert spectrogram.frequencies is not None
    assert spectrogram.times is not None
    assert spectrogram.power is not None