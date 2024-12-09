import os, sys
from os.path import dirname as up

sys.path.append(os.path.abspath(os.path.join(up(__file__), os.pardir)))

from image_classification import SYSTEM_PROMPT, USER_PROMPT
import ollama

import re

from custom_logger import logger

from image_classification import SYSTEM_PROMPT, USER_PROMPT
from image_classification import animal_classifier_ollama, animal_classifier_openai, animal_classifier_gemini

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

def animal_classifier(model: str, image_path: str) -> str:
    """
    Classify animals in images using the specified model.
    
    Args:
        model (str): Name of the model to use
        image_path (str): Path to the image file
        
    Returns:
        str: Classification response from the model
    """
    if 'gpt' in model.lower():
        logger.info(f"Using OpenAI model: {model}")
        return animal_classifier_openai(model=model, image_path=image_path, system_prompt=SYSTEM_PROMPT, user_prompt=USER_PROMPT)
    elif 'gemini' in model.lower():
        logger.info(f"Using Gemini model: {model}")
        return animal_classifier_gemini(model=model, image_path=image_path, system_prompt=SYSTEM_PROMPT, user_prompt=USER_PROMPT)
    return animal_classifier_ollama(model=model, image_path=image_path, system_prompt=SYSTEM_PROMPT, user_prompt=USER_PROMPT)

