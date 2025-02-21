from sklearn.metrics import mean_squared_error, mean_absolute_error
import numpy as np

def evaluate_model(model, X_test, y_test):
    """
    Avalia o desempenho do modelo LSTM no conjunto de testes.

    :param model: Modelo LSTM treinado
    :param X_test: Dados de entrada para o teste
    :param y_test: Valores reais de saída para o teste
    :return: Erro quadrático médio (MSE) e erro absoluto médio (MAE)
    """
    # Fazendo previsões com o modelo treinado
    y_pred = model.predict(X_test)
    
    # Calculando o erro quadrático médio (MSE)
    mse = mean_squared_error(y_test, y_pred)
    
    # Calculando o erro absoluto médio (MAE)
    mae = mean_absolute_error(y_test, y_pred)
    
    print(f'Erro Quadrático Médio (MSE): {mse}')
    print(f'Erro Absoluto Médio (MAE): {mae}')
    
    return mse, mae
