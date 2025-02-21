import pandas as pd

def convert_to_datetime(df, column_name='recvTime'):
    """
    Converte uma coluna para o formato datetime.

    :param df: DataFrame com os dados
    :param column_name: Nome da coluna a ser convertida
    :return: DataFrame com a coluna convertida
    """
    df[column_name] = pd.to_datetime(df[column_name], errors='coerce')
    return df
