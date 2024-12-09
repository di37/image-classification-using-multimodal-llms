import os, sys
from os.path import dirname as up

sys.path.append(os.path.abspath(os.path.join(up(__file__), os.pardir)))

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
)
from typing import Dict

def compute_multiclass_metrics(y_true, y_pred, average='macro'):
    """
    Computes various multi-class classification metrics.
    
    Args:
        y_true (array-like): True labels.
        y_pred (array-like): Predicted labels.
        average (str): Averaging method for precision, recall, and F1-score.
                       Can be 'micro', 'macro', 'weighted', or None.
    
    Returns:
        dict: Dictionary containing the computed metrics.
    """
    accuracy = accuracy_score(y_true, y_pred)
    precision = precision_score(y_true, y_pred, average=average)
    recall = recall_score(y_true, y_pred, average=average)
    f1 = f1_score(y_true, y_pred, average=average)
    cm = confusion_matrix(y_true, y_pred)
    
    metrics = {
        'accuracy': accuracy,
        'precision': precision,
        'recall': recall,
        'f1': f1,
        # 'confusion_matrix': cm
    }
    
    return metrics

def plot_confusion_matrix(true_category, predicted_category, category_name):
    cm = confusion_matrix(true_category, predicted_category)
    labels = sorted(set(true_category))
    
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=labels, yticklabels=labels)
    plt.xlabel('Predicted Labels')
    plt.ylabel('True Labels')
    plt.title(f'Confusion Matrix - {category_name}')
    plt.show()