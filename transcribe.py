import whisper

model = whisper.load_model("base.en")

mp3 = "TestFiles\y2mate.com - Smash Ultimate Art of Incineroar.mp3"
result = model.transcribe(mp3, language = "en", fp16 = False)
print(result["text"])

file_path = "Transcriptions\TranscribedAudio.txt"
with open(file_path, 'w') as file:
    # Write content to the file
    file.write(result["text"])