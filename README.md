# Evaluating Multimodal LLMs on Image Classification: A Comparative Analysis of Open-Source and Proprietary Models

**Short Description:**  
This project evaluates and compares the performance of various multimodal Large Language Models (LLMs)—both open-source and closed-source—on an animal image classification task. The repository demonstrates data sampling, model inference, output normalization, and comprehensive evaluation of accuracy, precision, recall, and F1 scores. It also explores trade-offs in inference time, data handling, and output formatting, ultimately providing insights into how different models fare in visual classification.

---

## Key Features

- **Multimodal Image Classification:**  
  Leverages LLMs that can process visual input to classify a curated set of animal images.
  
- **Variety of Models:**  
  Tests both open-source models (e.g., LLaMA variants, minicpm-v) and closed-source models (e.g., Gemini, GPT-4o) to highlight differences in performance, format consistency, and inference speed.

- **Normalization of Outputs:**  
  Implements post-processing steps to correct misspellings, verbose labels, or truncated predictions, ensuring fair and accurate metric comparisons.

- **Metrics & Visualizations:**  
  Provides accuracy, precision, recall, and F1 scores, alongside confusion matrices and inference time statistics to offer a complete performance profile.

---

## Repository Structure

- **`custom_logger/`**  
  Contains custom logging utilities that provide consistent, structured logs throughout the codebase.
  
- **`data/`**  
  Holds input data files and model-generated results.  
  - **`results_*.csv`:** Classification outputs for each model family (ollama, gemini, openai).  
  - **`sampled_animals.csv`:** Lists the subset of animals and images selected for evaluation.

- **`image_classification/`**  
  Contains core logic for performing image classification using various models, handling prompts, and evaluating outputs.

- **`notebooks/`**  
  Jupyter notebooks outlining each stage of the workflow:  
  1. **Data Gathering & Sampling:** Selecting a subset of animal images.  
  2. **Image Classification:** Running images through all models.  
  3. **Data Normalization:** Cleaning and standardizing outputs.  
  4. **Model Evaluation:** Computing metrics, plotting confusion matrices, and analyzing results.

- **`utilities/`**  
  Provides helper scripts, constants, and command-line utilities (that simplify repetitive tasks and support the main codebase.

- **`classify.py`**  
  A script to run classification across various models, generating CSV results.

- **`.env` & Configuration Files:**  
  May store environment variables or keys required to access closed-source models.

- **`README.md`** (this file):  
  A high-level overview of the entire project, guiding users through setup and usage.

---

## Getting Started

**Prerequisites:**

- Python 3.10+  
- A virtual environment (recommended)
- Required packages listed in `requirements.txt` (if provided).

**Installation Steps:**

1. Clone the repository:
   ```bash
   git clone https://github.com/di37/multimodal-image-classification.git
   ```
2. Change into the project directory:
   ```bash
   cd multimodal-image-classification
   ```
3. Set up a virtual environment and install dependencies:
   ```bash
   conda create -n image_classification python=3.10
   conda activate image_classification
   pip install -r requirements.txt
   ```
4. Add any necessary API keys or model credentials to your `.env` file.

---

## Usage

1. **Data Preparation:**  
   Use `01_Data_Gathering_And_Sampling.ipynb` in `notebooks/` to generate `sampled_animals.csv`.

2. **Classification:**  
   Run the classification script to process all images:
   ```bash
   python classify.py
   ```
   This will invoke all models (open-source and closed-source) and store results in the `data/` directory.

3. **Normalization:**  
   Use `03_Data_Normalization_of_Outputs.ipynb` to clean and standardize outputs from models that require it (e.g., Ollama models).

4. **Evaluation:**  
   Finally, run `04_Models_Evaluation.ipynb` to compute metrics, generate confusion matrices, compare inference times, and produce a comprehensive report of each model’s performance.

---

## Results and Interpretation

- **Performance Metrics:**  
  The evaluation notebooks summarize accuracy, precision, recall, and F1. Additional charts (e.g., confusion matrices, bar plots) are generated to visualize each model’s strengths and weaknesses.

- **Impact of Normalization:**  
  By comparing pre- and post-normalization results for open source models, users can see how minor formatting issues influenced initial metrics, uncovering the true capability of open-source models.

- **Trade-Offs:**  
  Closed-source models may yield perfect results but at higher latency and possibly less flexibility. Open-source models run locally and faster but may need some refinement and prompt tuning.

Please read the article for in-depth analysis:

---

## Contributing

Contributions are welcome. Please open an issue or submit a pull request if you have improvements, bug fixes, or new features to propose.

---

## Acknowledgments

- **Data:** Sourced from Kaggle’s animal images dataset.
- **Models:**  
  - Open-Source: `LlaVa` variants, `Llama` models and `minicpm-v`  
  - Closed-Source: Gemini, GPT-4o, etc.
- **Community:** Thanks to the open-source community and model developers for providing the tools and resources enabling this project.

---

*This README provides a roadmap for anyone looking to understand, reproduce, or build upon the project.*