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
    # try:
    audio_file = request.files['audioFile'] 
    if audio_file:
        whisper_asr = pipeline("automatic-speech-recognition", model="openai/whisper-base")
        transcription = whisper_asr(audio_file.read())['text']
        
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a student that writes detailed bulleted lecture notes."},
                {"role": "user", "content": transcription},
                {"role": "assistant", "content": "Generate detailed bulleted lecture notes and 5 practice problems based on the lecture."}
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
        print(jsonify(response_data))
        return jsonify(response_data)
    # except Exception as e:
    #     print(f"Error processing request: {e}")
    #     return jsonify({'error': 'Internal server error'})

# @app.route('/generate_summary_and_questions', methods=['POST'])
# def generate_summary_and_questions():
#     try:
#         audio_text = request.form.get('audio_text')

#         # Make a request to ChatGPT-3.5 API for summarization and practice problems generation
#         response = openai.ChatCompletion.create(
#             model="gpt-3.5-turbo",
#             messages=[
#                 {"role": "system", "content": "You are a student that writes detailed bulleted lecture notes."},
#                 {"role": "user", "content": audio_text},
#                 {"role": "assistant", "content": "Generate detailed bulleted lecture notes and 5 practice problems based on the lecture."}
#             ],
#             api_key=api_key
#         )

#         # Extract summary and practice problems from API response
#         content = response.choices[0].message['content']
#         practice_problems_start = content.find("Practice Problems:")
#         summary = content[:practice_problems_start].strip()
#         practice_problems = content[practice_problems_start + len("Practice Problems:"):].strip().split("\n")

#         # Format practice problems as a list of questions
#         questions = [problem.replace(str(idx) + ".", "").strip() for idx, problem in enumerate(practice_problems, start=1)]

#         # Prepare the response
#         response_data = {
#             "summary": summary,
#             "questions": questions
#         }

#         return jsonify(response_data)

#     except Exception as e:
#         error_message = f"An error occurred: {str(e)}"
#         return jsonify({"error": error_message}), 500

if __name__ == '__main__':
    app.run(debug=True)
