import pandas as pd

def clean_data(df):
    """
    Limpeza básica dos dados:
    - Remover colunas desnecessárias
    - Converter colunas para tipos adequados

    :param df: DataFrame com os dados carregados
    :return: DataFrame limpo
    """
    # Remover a coluna '_id' como exemplo
    df = df.drop(columns=['_id'])

    # Converter a coluna 'recvTime' para datetime
    df['recvTime'] = pd.to_datetime(df['recvTime'], errors='coerce')

    # Verificar se há dados inválidos após conversão
    df = df.dropna(subset=['recvTime'])

    return df
