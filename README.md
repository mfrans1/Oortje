# Oortje - Bird Call Identification Tool

Oortje means little ear in dutch.

I've been an avid user of birding apps like [merlin](https://www.merlinbirds.org/) for years now, and always wondered how they worked at a high level. This repo is a small project exploring that idea a bit more. 

Oortje is a tool that ingests wav recordings of bird calls, and (will in the end) give you a top 3 possibilities of birds you could be listening to (of course depending on the training data you've ingested at that point). Thinking merlin but less effective in almost every way. 

## How it works
Input bird call recordings (`.wav` files) are transforemd to spectrograms, and calls are isolated from background noise using a basic median filtering algorithm. This removes redundant data and allows the use of `scipy.ndimage` labelling to then decompose the calls into individual features. 
[](data/plots/spectrogram.png)
[](data/plots/spectrogram_clean.png)
[](data/plots/spectrogram_features.png)

## Data Sources
All the bird recordings I applied for the project were through this [repository](https://dl.allaboutbirds.org/backyardbirdsdownload-0), because I wanted to stay with the Cornell Lab for Ornithology. 

But it's very easy to expand the project with more recordings, this ended up being quite small. If the project ever takes a more complex (deep learning) approach, it might be necessary to expand the dataset using recordings from [xeno-canto](https://xeno-canto.org/) or similar. But for now it's just a hobby...