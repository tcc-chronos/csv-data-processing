import pandas as pd

def convert_column_to_numeric(df, column_name):
    """
    Converte uma coluna para tipo numérico, caso seja possível.

    :param df: DataFrame com os dados
    :param column_name: Nome da coluna a ser convertida
    :return: DataFrame com a coluna convertida
    """
    df[column_name] = pd.to_numeric(df[column_name], errors='coerce')
    return df

def parse_datetime_column(df, column_name):
    """
    Converte uma coluna para o formato datetime.

    :param df: DataFrame com os dados
    :param column_name: Nome da coluna a ser convertida
    :return: DataFrame com a coluna convertida para datetime
    """
    df[column_name] = pd.to_datetime(df[column_name], errors='coerce')
    return df
