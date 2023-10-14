from fastapi import FastAPI, Form
from fastapi.responses import JSONResponse
import openai

app = FastAPI()

# Set your OpenAI API key here
api_key = "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"

@app.post("/chat")
async def genResponse(audio_text: str = Form(...), question: str = Form(...)):
    try:
        # Use the stored lecture transcript to answer the question
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": """A lecture transcript will be entered. Please answer the following questions ONLY using information from the provided lecture. Do NOT use any information other than what is provided in the lecture."""},
                {"role": "user", "content": audio_text},
                {"role": "user", "content": question}
            ],
            api_key=api_key,
            temperature=0.7,
            max_tokens=150,
            stop=None
        )
        return JSONResponse(content=response)
    except Exception as e:
        error_message = f"An error occurred: {str(e)}"
        return JSONResponse(content={"error": error_message}, status_code=500)
