import openai

# Set your OpenAI API key here
api_key = "API_KEY"

file_path = "Transcriptions/TranscribedAudio.txt"
output_file_path = "summary.txt"  # Path to save the summary
practice_problems_file_path = "practice_problems.txt"  # Path to save the practice problems

# Read the lecture text from a text file
try:
    with open(file_path, "r") as file:
        lecture_text = file.read().strip()
except FileNotFoundError:
    print("Error: Lecture text file not found.")
    exit()
except Exception as e:
    print(f"An error occurred: {str(e)}")
    exit()

# Check if lecture text is empty
if not lecture_text:
    print("Error: Lecture text is empty.")
    exit()

# Make a request to ChatGPT-3.5 API for both summarization and practice problems generation
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": """You are a student that writes detailed bulleted lecture notes."""},
        {"role": "user", "content": lecture_text},
        {"role": "assistant", "content": "Generate detailed bulleted lecture notes and 5 practice problems based on the lecture."}
    ],
    api_key=api_key
)

try:
    # Extract summary and practice problems from API response
    content = response.choices[0].message['content']
    
    # Find the index of Practice Problems: and split accordingly
    practice_problems_start = content.find("Practice Problems:")
    summary = content[:practice_problems_start].strip()
    practice_problems = content[practice_problems_start + len("Practice Problems:"):].strip().split("\n")

    # Print the summary and practice problems
    print("Summarized Lecture:")
    print(summary)
    print("Practice Problems:")
    for idx, problem in enumerate(practice_problems, start=1):
        print(f"{problem}")

    # Write the summary to a text file
    with open(output_file_path, "w") as summary_file:
        summary_file.write(summary)
    print(f"Summary written to {output_file_path}")

    # Write the practice problems to a text file
    with open(practice_problems_file_path, "w") as problems_file:
        for idx, problem in enumerate(practice_problems, start=1):
            problems_file.write(f"\n{problem}")
    print(f"Practice problems written to {practice_problems_file_path}")

except KeyError:
    print("Error: Unexpected API response format.")
    exit()
