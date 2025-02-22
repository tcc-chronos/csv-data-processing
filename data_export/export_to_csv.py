import pandas as pd

def export_to_csv(df: pd.DataFrame, file_path: str, sep: str = ';', index: bool = True):
    """
    Realiza a exportação de um DataFrame para o arquivo CSV especificado.

    :param df: DataFrame com os dados carregados
    :param file_path: Caminho do arquivo CSV
    :param sep: Separador dos dados no arquivo CSV (padrão: ';')
    :param index: Indica se o índice do DataFrame será exportado como uma coluna no arquivo CSV (padrão: True, para manter o recvTime)
    """
    try:
        df.to_csv(file_path, sep=sep, index=index)
        print(f"Arquivo salvo com sucesso em: {file_path}")
    except FileNotFoundError:
        print(f"Erro: O diretório especificado para '{file_path}' não existe.")
    except PermissionError:
        print(f"Erro: Permissão negada para escrever no arquivo '{file_path}'. Feche o arquivo se ele estiver aberto.")
    except AttributeError:
        print("Erro: O objeto fornecido não é um DataFrame válido.")
    except IOError as e:
        print(f"Erro de E/S ao tentar salvar o arquivo: {e}")
    except Exception as e:
        print(f"Erro inesperado: {e}")
