# Image Classification folder - `image_classification`
 
**Purpose:**  
This directory encapsulates the code related to the image classification logic, prompt formulation, and evaluation utilities. It focuses on how images are turned into predictions using various LLM-based models.

**Key Files:**

- `classifiers.py`:  
  Defines wrapper classes or functions that interact with different models (open-source or closed-source) to perform image classification.

- `evaluation.py`:  
  Provides functions to compute metrics (accuracy, precision, recall, F1) and generate confusion matrices.

- `prompts.py`:  
  Contains standardized prompt templates or instructions used by the LLMs when classifying images. Adjust these to influence how models interpret images.

- `__init__.py`:  
  Makes this directory a Python package, enabling modular imports.

**How to Use:**

1. **Classification:**  
   ```python
   from image_classification import animal_classifier_ollama
   label = animal_classifier_ollama(model='llama3.2-vision', image_path='path/to/image.jpg', system_prompt=SYSTEM_PROMPT, user_prompt=USER_PROMPT) 
   ```

2. **Evaluation:**  
   ```python
   from image_classification import compute_multiclass_metrics
   metrics = compute_multiclass_metrics(y_true, y_pred)
   print(metrics)
   ```

3. **Prompt Customization:**  
   Edit `prompts.py` to modify the prompt to get the best possible result for image classification.

**Notes:**  
- Keep model-specific logic separated for easier maintenance.
- The code here should be model-agnostic where possible, relying on abstract interfaces.