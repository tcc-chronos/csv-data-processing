import pandas as pd

def load_data(file_path: str):
    """
    Carrega o dataset a partir do arquivo CSV fornecido.

    :param file_path: Caminho do arquivo CSV
    :return: DataFrame com os dados carregados ou None em caso de erro
    """
    try:
        data = pd.read_csv(file_path)
        print(f"Arquivo '{file_path}' carregado com sucesso.\n")
        return data
    except FileNotFoundError:
        print(f"Erro: O arquivo '{file_path}' não foi encontrado.")
    except PermissionError:
        print(f"Erro: Permissão negada para acessar o arquivo '{file_path}'. Verifique se ele está aberto.")
    except pd.errors.EmptyDataError:
        print(f"Erro: O arquivo '{file_path}' está vazio.")
    except pd.errors.ParserError:
        print(f"Erro: O arquivo '{file_path}' contém dados inválidos ou mal formatados.")
    except Exception as e:
        print(f"Erro inesperado ao carregar o arquivo '{file_path}': {e}")
    
    return None
