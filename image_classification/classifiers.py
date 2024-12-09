import os, sys
from os.path import dirname as up

sys.path.append(os.path.abspath(os.path.join(up(__file__), os.pardir)))

import ollama 
import re

import base64
from openai import OpenAI

import google.generativeai as genai
from PIL import Image
from dotenv import load_dotenv

_ = load_dotenv()

def animal_classifier_ollama(model: str, image_path: str, system_prompt: str, user_prompt: str) -> str:
    """
    Classify animals in images using Ollama model.
    
    Args:
        model (str): Name of the Ollama model to use
        image_path (str): Path to the image file
        system_prompt (str): System prompt for the model
        user_prompt (str): User prompt for the model
        
    Returns:
        str: Classification response from the model
    """
    try:
        messages = [{
            'role': 'system',
            'content': system_prompt
        }, {
            'role': 'user',
            'content': user_prompt,
            'images': [image_path]
        }]
        
        # Make API call to Ollama
        response = ollama.chat(
            model=model,
            messages=messages,
        )
        
        response = response.message.content
        cleaned_response = re.sub(r'[^a-zA-Z]', '', response.strip().lower())
        return cleaned_response

    except Exception as e:
        print(f"Error in animal classification: {str(e)}")
        return f"Error: {str(e)}"
    
def animal_classifier_openai(model: str, image_path: str, system_prompt: str, user_prompt: str) -> str:
    """
    Classify animals in images using OpenAI model.
    
    Args:
        model (str): Name of the OpenAI model to use
        image_path (str): Path to the image file
        system_prompt (str): System prompt for the model
        user_prompt (str): User prompt for the model
        
    Returns:
        str: Classification response from the model
    """
    client = OpenAI()

    # Function to encode the image
    def encode_image(image_path):
      with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

    # Getting the base64 string
    base64_image = encode_image(image_path)

    response = client.chat.completions.create(
      model=model,
      messages=[
        {
          "role": "user",
          "content": [
            {
              "type": "text",
              "text": system_prompt + user_prompt,
            },
            {
              "type": "image_url",
              "image_url": {
                "url":  f"data:image/jpeg;base64,{base64_image}"
              },
            },
          ],
        }
      ],
    )
    response = response.choices[0].message.content
    cleaned_response = re.sub(r'[^a-zA-Z]', '', response.strip().lower())
    return cleaned_response

def animal_classifier_gemini(model: str, image_path: str, system_prompt: str, user_prompt: str) -> str:
    """
    Classify animals in images using Gemini model.
    
    Args:
        model (str): Name of the Gemini model to use
        image_path (str): Path to the image file
        system_prompt (str): System prompt for the model
        user_prompt (str): User prompt for the model
        
    Returns:
        str: Classification response from the model
    """
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
    genai.configure(api_key=GOOGLE_API_KEY)
    image = Image.open(image_path)
    model = genai.GenerativeModel(model_name = model)
    prompt = system_prompt + user_prompt
    response = model.generate_content([image, prompt])
    cleaned_response = re.sub(r'[^a-zA-Z]', '', response.text.strip().lower())
    return cleaned_response