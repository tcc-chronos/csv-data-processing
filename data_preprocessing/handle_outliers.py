import numpy as np
import pandas as pd
from scipy.stats import zscore

def handle_outliers(df, threshold=3):
    """
    Identifica e remove outliers usando o Z-score.

    :param df: DataFrame com os dados
    :param threshold: Limite do Z-score para considerar um valor como outlier
    :return: DataFrame sem outliers
    """
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    df_zscore = df[numeric_cols].apply(zscore)

    # Remover linhas com outliers (Z-score > threshold ou < -threshold)
    df_no_outliers = df[(np.abs(df_zscore) < threshold).all(axis=1)]

    return df_no_outliers
