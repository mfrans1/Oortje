for f in data/mp3/*.mp3; do
    ffmpeg -i "$f" "data/wav/$(basename "${f%.mp3}").wav"
done
