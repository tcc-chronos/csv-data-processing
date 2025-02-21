import pandas as pd

def load_data(file_path):
    """
    Carrega o dataset a partir do arquivo CSV fornecido.

    :param file_path: Caminho do arquivo CSV
    :return: DataFrame com os dados carregados
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        print(f"Erro ao carregar os dados: {e}")
        return None
