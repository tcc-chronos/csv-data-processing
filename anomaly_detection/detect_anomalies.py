import pandas as pd
import numpy as np
from scipy.stats import zscore

def detect_anomalies(df, threshold=3):
    """
    Detecta anomalias em variáveis numéricas utilizando Z-score.

    :param df: DataFrame com os dados
    :param threshold: Limite do Z-score para considerar um valor como anômalo
    :return: DataFrame com as anomalias detectadas
    """
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    df_zscore = df[numeric_cols].apply(zscore)

    # Detectar anomalias (Z-score > threshold ou < -threshold)
    anomalies = (np.abs(df_zscore) > threshold).any(axis=1)
    
    return df[anomalies]
