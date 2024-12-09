import os, sys
from os.path import dirname as up

sys.path.append(os.path.abspath(os.path.join(up(__file__), os.pardir)))

MODELS_OLLAMA = ['llama3.2-vision', 'minicpm-v', 'llava-llama3', 'llava', 'llava:13b']
MODELS_OPENAI = ['gpt-4o-mini', 'gpt-4o']
MODELS_GEMINI = ['gemini-1.5-pro', 'gemini-1.5-flash-8b', 'gemini-1.5-flash']
SAMPLED_ANIMALS_PATH = 'data/sampled_animals.csv'
RESULTS_PATH = 'data/results.csv'