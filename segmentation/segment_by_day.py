import pandas as pd

def segment_by_day(df):
    """
    Segmenta os dados por dia da semana e hora.

    :param df: DataFrame com os dados
    :return: DataFrame segmentado com colunas 'day_of_week' e 'hour_of_day'
    """
    # Adicionar colunas para o dia da semana e a hora do dia
    df['recvTime'] = pd.to_datetime(df['recvTime'], errors='coerce')
    df['day_of_week'] = df['recvTime'].dt.dayofweek  # 0: segunda-feira, 6: domingo
    df['hour_of_day'] = df['recvTime'].dt.hour  # Hora no dia (0-23)
    
    # Agrupar os dados por dia da semana e hora, para análise ou segmentação
    df_segmented = df.groupby(['day_of_week', 'hour_of_day']).agg(list).reset_index()

    return df_segmented
