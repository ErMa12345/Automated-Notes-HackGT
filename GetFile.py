from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_file():
    try:
        # Get the uploaded file
        uploaded_file = request.files['file']

        # Save the file to a specific directory (you might want to change this)
        file_path = os.path.join('uploads', uploaded_file.filename)
        uploaded_file.save(file_path)

        return jsonify({'message': 'File uploaded successfully', 'file_path': file_path})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
