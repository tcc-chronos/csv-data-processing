import os
from tensorflow.keras.models import load_model

def save_model(model, model_name='lstm_model.h5'):
    """
    Salva o modelo treinado em um arquivo.

    :param model: Modelo LSTM treinado
    :param model_name: Nome do arquivo para salvar o modelo
    """
    if not os.path.exists('models'):
        os.makedirs('models')
    model.save(os.path.join('models', model_name))
    print(f'Modelo salvo em {os.path.join("models", model_name)}')

def load_saved_model(model_name='lstm_model.h5'):
    """
    Carrega um modelo treinado a partir de um arquivo.

    :param model_name: Nome do arquivo do modelo a ser carregado
    :return: Modelo LSTM carregado
    """
    model_path = os.path.join('models', model_name)
    if os.path.exists(model_path):
        model = load_model(model_path)
        print(f'Modelo carregado de {model_path}')
        return model
    else:
        print(f'Arquivo {model_path} não encontrado!')
        return None
