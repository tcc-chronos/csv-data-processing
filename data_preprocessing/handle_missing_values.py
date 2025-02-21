import pandas as pd

def handle_missing_values(df, strategy='mean'):
    """
    Trata os valores ausentes usando uma estratégia específica.

    :param df: DataFrame com os dados limpos
    :param strategy: Estratégia para imputação (opções: 'mean', 'median', 'drop')
    :return: DataFrame com valores ausentes tratados
    """
    if strategy == 'mean':
        df = df.fillna(df.mean())
    elif strategy == 'median':
        df = df.fillna(df.median())
    elif strategy == 'drop':
        df = df.dropna()
    else:
        print("Estratégia inválida. Usando a média por padrão.")
        df = df.fillna(df.mean())
    
    return df
