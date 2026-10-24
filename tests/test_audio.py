from oortje.audio import Audio


def test_audio_initialization():

    # Test with an invalid file path
    try:
        Audio("invalid/path/to/audio.wav")
        raise AssertionError("Expected FileNotFoundError")
    except FileNotFoundError:
        pass