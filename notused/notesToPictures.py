from diffusers import StableDiffusionPipeline
import torch
import requests
import os

model_id = "runwayml/stable-diffusion-v1-5"
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
pipe = pipe.to("cuda")

#generate images from notes line by line (?)
def generateImages(inputArr):
    for prompt in inputArr:
        image = pipe(prompt).images[0]
        print(image)

string_array = ["apple", "banana", "orange", "grape"]
generateImages(string_array)

# prompt = "a photo of an astronaut riding a horse on mars"
# image = pipe(prompt).images[0]  
    
# image.save("astronaut_rides_horse.png")
