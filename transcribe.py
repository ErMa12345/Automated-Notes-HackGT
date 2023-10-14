import whisper

model = whisper.load_model("base.en")

mp3 = "testFiles\y2mate.com - Smash Ultimate Art of Incineroar.mp3"
result = model.transcribe(mp3, language = "en", fp16 = False)
print(result["text"])
# print(len(result))

# file_path = 'example.txt'

# with open(file_path, 'w') as file:
#     # Write content to the file
#     file.write(result.text)
   
# print(f"Text has been written to {file_path}")

