import soundfile as sf

class Audio:
    def __init__(self, 
                 file_path: str):
        """
        Initialize the Audio object by loading in audio data
        from filepath using soundfile. Default behaviour for now
        is to convert to mono if audio has multiple channels.
        """
        self.data, self.sample_rate = sf.read(file_path)

        if self.data.ndim > 1:
            # If the audio has multiple channels, take the mean to convert to mono
            self.data = self.data.mean(axis=1)

    @property
    def duration(self):
        """Duration of the audio recording in seconds."""
        return len(self.data) / self.sample_rate

    @property
    def number_of_samples(self):
        """Number of samples in the audio recording."""
        return len(self.data)

    def save(self, file_path: str):
        """Save the audio data to a file."""
        sf.write(file_path, self.data, self.sample_rate)
        print(f"Saved audio to: {file_path}")