import pandas as pd

def parse_and_segment(df, column_name='recvTime'):
    """
    Converte a coluna de data e segmenta os dados por hora e dia da semana.

    :param df: DataFrame com os dados
    :param column_name: Nome da coluna com timestamps (padrão: 'recvTime')
    :return: DataFrame com dados segmentados
    """
    df[column_name] = pd.to_datetime(df[column_name], errors='coerce')
    df['day_of_week'] = df[column_name].dt.dayofweek  # 0: segunda-feira, 6: domingo
    df['hour_of_day'] = df[column_name].dt.hour  # Hora no dia (0-23)
    
    return df
