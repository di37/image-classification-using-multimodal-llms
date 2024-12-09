### Data folder - `data` 

**Purpose:**  
This folder holds all data files and datasets used for the project, including input image labels, sampled subsets of animals, and model classification results. It serves as the central repository for raw and intermediate data.

**Key Files and Directories:**

- `animals/`:  
  Due to image files being very heavy, we are not pushing it in the github. But here the images of all  90 `animals` are stored here along with their names. 

- `results_gemini.csv`:  
  Classification results obtained from the Gemini models.

- `results_ollama.csv` & `results_ollama_cleaned.csv`:  
  Results from the Ollama (local) models. `results_ollama_cleaned.csv` is the post-normalization version, showing corrected labels for fair evaluation.

- `results_openai.csv`:  
  Contains classification outputs from OpenAI’s models.

- `sampled_animals.csv`:  
  List of selected animal classes and sampled image filenames for the evaluation subset.

**Usage:**

- Use `sampled_animals.csv` as a reference for which images to process.
- Compare `results_ollama.csv` and `results_ollama_cleaned.csv` to understand the impact of normalization.
- `results_openai.csv` and `results_gemini.csv` can be used to benchmark closed-source model performance.

**Notes:**  
- Ensure that the data files are not tampered with to maintain reproducibility.
- If large raw image datasets are used, they may be stored externally, and `animals` here might just contain references or metadata.
