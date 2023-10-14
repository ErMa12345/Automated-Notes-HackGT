import whisper
import numpy as np
from transformers import pipeline

model = pipeline("automatic-speech-recognition", model="openai/whisper-base")

def transcribeEric(file):
    print("transcribing now")
    print(file)
    mp3 = file.files['audioFile'] 
    print(mp3)
    # mp3 = np.loadtxt(file)
    # print(mp3)
    result = model(mp3.read())
    print(result["text"])
    file_path = "Transcriptions\TranscribedAudio.txt"
    with open(file_path, 'w') as file:
        # Write content to the file
        file.write(result["text"])
