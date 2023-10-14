
from fastapi import FastAPI, Request, Form
from fastapi.responses import JSONResponse
import openai

app = FastAPI()

# Set your OpenAI API key here
api_key = "API_KEY"

@app.post("/generate_summary_and_questions")
async def generate_summary_and_questions(audio_text: str = Form(...)):
    try:
        # Make a request to ChatGPT-3.5 API for summarization and practice problems generation
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": """You are a student that writes detailed bulleted lecture notes."""},
                {"role": "user", "content": audio_text},
                {"role": "assistant", "content": "Generate detailed bulleted lecture notes and 5 practice problems based on the lecture."}
            ],
            api_key=api_key
        )

        # Extract summary and practice problems from API response
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

        return JSONResponse(content=response_data)

    except Exception as e:
        error_message = f"An error occurred: {str(e)}"
        return JSONResponse(content={"error": error_message}, status_code=500)

"""@app.post("/ask_question")
async def ask_question(audio_text: str = Form(...), question: str = Form(...)):
    try:
        # Calculate similarity score between user's question and lecture text
        question_doc = nlp(question)
        lecture_doc = nlp(audio_text)
        similarity_score = question_doc.similarity(lecture_doc)

        # Set a similarity threshold (you can adjust this based on your needs)
        similarity_threshold = 0.8

        # Only answer questions with similarity above the threshold
        if similarity_score >= similarity_threshold:
            # Make a request to ChatGPT-3.5-Turbo API for answering the user's question
            response = openai.Completion.create(
                engine="gpt-3.5-turbo",
                prompt=f"Q: {question}\nA:",
                max_tokens=150,
                api_key=api_key
            )

            # Extract the answer from API res
            answer = response.choices[0].text.strip()

            # Prepare the response
            response_data = {
                "answer": answer
            }

            return JSONResponse(content=response_data)
        else:
            # Return a message indicating the question is not relevant to the lecture text
            return JSONResponse(content={"error": "Question is not relevant to the lecture text."}, status_code=400)

    except Exception as e:
        error_message = f"An error occurred: {str(e)}"
        return JSONResponse(content={"error": error_message}, status_code=500)"""
