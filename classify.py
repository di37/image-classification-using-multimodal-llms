from utilities import MODELS_OPENAI, MODELS_GEMINI, MODELS_OLLAMA, SAMPLED_ANIMALS_PATH
from utilities import animal_classifier

from custom_logger import logger

import pandas as pd
import time
from tqdm import tqdm


# Define all models in a single dictionary for better structure
all_models = {
    "ollama": MODELS_OLLAMA,
    "gemini": MODELS_GEMINI,
    "openai": MODELS_OPENAI,
}

# Process each model
for manufacturer, models in all_models.items():
    for model in models:
        # Load dataset
        try:
            df = pd.read_csv(SAMPLED_ANIMALS_PATH)
            logger.info(f"Successfully loaded dataset with {len(df)} images")
        except Exception as e:
            logger.error(f"Failed to load dataset: {str(e)}")
            raise
        
        # Start classification
        start_time = time.time()
        logger.info(f"Starting classification with model: {model}")
        
        df[f'{model.lower()}_result'] = None
        results = []
        elapsed_times = []
        
        # Process each image with progress bar
        for index, row in tqdm(df.iterrows(), total=len(df), desc=f"Processing {model}"):
            animal = row['animal']
            image_path = row['path']
            
            try:
                logger.debug(f"Classifying image {index+1}/{len(df)}: {image_path}")
                start_time_in = time.time()
                result = animal_classifier(model=model, image_path=image_path)
                results.append(result)
                elapsed_times.append(time.time() - start_time_in)
            
            except Exception as e:
                logger.error(f"Error processing image {image_path} with {model}: {str(e)}")
                results.append("Error in classification")
                
        df[f'{model.lower()}_result'] = results
        df[f'{model.lower()}_elapsed_time'] = elapsed_times
        
        # Log completion time for model
        elapsed_time = time.time() - start_time
        logger.info(f"Completed {model} classification in {elapsed_time:.2f} seconds")
        logger.info(f"Successfully processed {len(results)} images with {model}")

    # Save results
    try:
        results_path = f'data/results_{manufacturer}.csv'
        logger.info(f"Saving results to: {results_path}")
        df.to_csv(results_path, index=False)
        logger.info("Results saved successfully")
    except Exception as e:
        logger.error(f"Failed to save results: {str(e)}")
        raise

    logger.info("Classification process completed")