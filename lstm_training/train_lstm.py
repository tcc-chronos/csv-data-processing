import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout

def train_lstm(X_train, y_train, epochs=50, batch_size=32):
    """
    Treina o modelo LSTM com os dados fornecidos.

    :param X_train: Dados de entrada para o treinamento
    :param y_train: Valores de saída para o treinamento
    :param epochs: Número de épocas para treinamento
    :param batch_size: Tamanho do batch para treinamento
    :return: Modelo treinado
    """
    model = Sequential()
    model.add(LSTM(units=50, return_sequences=True, input_shape=(X_train.shape[1], X_train.shape[2])))
    model.add(Dropout(0.2))
    model.add(LSTM(units=50, return_sequences=False))
    model.add(Dropout(0.2))
    model.add(Dense(units=1))  # Prevendo uma variável contínua

    model.compile(optimizer='adam', loss='mean_squared_error')

    # Treinamento do modelo
    model.fit(X_train, y_train, epochs=epochs, batch_size=batch_size)

    return model
