from oortje.audio import Audio

def test_audio_initialization():
    # Test with a valid file path
    audio = Audio("data/wav/01 Eastern Backyard Birds.wav")
    assert audio.file_path.exists()
    assert audio.data is not None
    assert audio.sample_rate > 0

    # Test with an invalid file path
    try:
        Audio("invalid/path/to/audio.wav")
        assert False, "Expected FileNotFoundError"
    except FileNotFoundError:
        pass