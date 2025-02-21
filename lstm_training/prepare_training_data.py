import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def prepare_training_data(df, columns_to_use):
    """
    Prepara os dados para treinamento do LSTM, incluindo normalização.

    :param df: DataFrame com os dados
    :param columns_to_use: Lista com os nomes das colunas a serem usadas
    :return: Dados normalizados prontos para o treinamento
    """
    # Selecionar as colunas necessárias
    df = df[columns_to_use]

    # Normalizar os dados (0-1)
    scaler = MinMaxScaler(feature_range=(0, 1))
    df_scaled = scaler.fit_transform(df)

    # Preparar os dados de séries temporais
    X, y = [], []
    for i in range(len(df_scaled) - 1):
        X.append(df_scaled[i])
        y.append(df_scaled[i + 1, 0])  # Exemplo: Prevendo a próxima variável de interesse

    return np.array(X), np.array(y)
