from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route('/upload', methods=['POST'])
def upload_audio():
    try:
        # Check if the POST request has the file part
        if 'file' not in request.files:
            return jsonify({'error': 'No file part'})

        # Get the uploaded file
        uploaded_file = request.files['file']

        # Check if the file is allowed
        allowed_extensions = {'mp3', 'wav', 'ogg', 'webm'}
        if '.' not in uploaded_file.filename or \
                uploaded_file.filename.rsplit('.', 1)[1].lower() not in allowed_extensions:
            return jsonify({'error': 'Invalid file type. Allowed types: mp3, wav, ogg'})

        # Save the file to a specific directory (you might want to change this)
        file_path = os.path.join('uploads', uploaded_file.filename)
        uploaded_file.save(file_path)

        return jsonify({'message': 'File uploaded successfully', 'file_path': file_path})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
