"""
Image classification package for animal classification using multimodal models.
"""

from .prompts import SYSTEM_PROMPT, USER_PROMPT
from .evaluation import compute_multiclass_metrics, plot_confusion_matrix
from .classifiers import animal_classifier_ollama, animal_classifier_openai, animal_classifier_gemini