# this will be responsible for decomposing the spectrogram into something useful

# probobably using classes again

"""
decompositoin idea: 

now we have cleaned spectrograms, ie just valid 
data and nan otherwise. 

now we want to compare different spectrograms of different
birds and group them into different classes

probably easiest to do some level of unsupervised learning, ie clustering,
rather than something like cosine similarity

"""