from flask import Flask, request, jsonify
from flask_cors import CORS
from transcribe import *
import requests
import numpy as np
import pydub

app = Flask(__name__)
CORS(app)

@app.route('/upload-audio', methods=['POST'])
def upload_audio():
    try:
        object_url = request.files['audioFile'] 
        transcribeEric(request)
        return jsonify({'message': 'File location received successfully'})
    except Exception as e:
        print(f"Error processing request: {e}")
        return jsonify({'error': 'Internal server error'})

if __name__ == '__main__':
    app.run(debug=True)
