from flask import Flask, request, jsonify
from flask_cors import CORS
from transformers import pipeline
import whisper
import numpy as np

app = Flask(__name__)
CORS(app)

model = whisper.load_model("base.en")

@app.route('/upload-audio', methods=['POST'])
def upload_audio():
    try:
        audio_file = request.files['audioFile']
        if audio_file:
            whisper_asr = pipeline("automatic-speech-recognition", model="openai/whisper-base", chunk_length_s=30)
            transcription = whisper_asr(audio_file.read())
        
            return jsonify({'transcription': transcription['text']})
    except Exception as e:
        print(f"Error processing request: {e}")
        return jsonify({'error': 'Internal server error'})

if __name__ == '__main__':
    app.run(debug=True)