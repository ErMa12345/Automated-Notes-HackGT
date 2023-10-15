from flask import Flask, request, jsonify
from flask_cors import CORS
from transformers import pipeline
import openai

app = Flask(__name__)
CORS(app)

# Set your OpenAI API key here
api_key = "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"

@app.route('/upload-audio', methods=['POST'])
def upload_audio():
    try:
        audio_file = request.files['audioFile']
        if audio_file:
            whisper_asr = pipeline("automatic-speech-recognition", model="openai/whisper-base", chunk_length_s=30)
            transcription = whisper_asr(audio_file.read())
            print(transcription['text'])
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a student that writes detailed bulleted lecture notes."},
                    {"role": "user", "content": transcription['text']},
                    {"role": "assistant", "content": "Generate detailed bulleted lecture notes. Then generate 5 practice problems based on the lecture. Seperate the bulleted notes and problems with the key term 'Practice Problems:'"}
                ],
                api_key=api_key
            )

            content = response.choices[0].message['content']
            practice_problems_start = content.find("Practice Problems:")
            summary = content[:practice_problems_start].strip()
            practice_problems = content[practice_problems_start + len("Practice Problems:"):].strip().split("\n")

            # Format practice problems as a list of questions
            questions = [problem.replace(str(idx) + ".", "").strip() for idx, problem in enumerate(practice_problems, start=1)]

            # Prepare the response
            response_data = {
                "summary": summary,
                "questions": questions
            }
            return jsonify(response_data)
    except Exception as e:
        print(f"Error processing request: {e}")
        return jsonify({'error': 'Internal server error'})

@app.route('/ask_question', methods=['POST'])
def ask_question():
    try:
        # Get the question from the request form data
        question = request.form['question']

        # Create a chat conversation with OpenAI API
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that answers questions"},
                {"role": "user", "content": question},
            ],
            api_key=api_key
        )

        # Extract the answer from API response
        answer = response.choices[0].message['content'].strip()

        # Prepare the response
        response_data = {
            "answer": answer
        }
        return jsonify(response_data)

    except Exception as e:
        # Handle exceptions, log them, and return an error response if needed
        error_message = f"An error occurred: {str(e)}"
        return jsonify({"error": error_message}), 500

if __name__ == '__main__':
    app.run(debug=True)
