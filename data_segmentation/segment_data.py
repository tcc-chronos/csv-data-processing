import pandas as pd
from enum import Enum

class TimeSegment(Enum):
    DAY = "D"
    HOUR = "h"
    MINUTE = "min"
    SECOND = "s"
    WEEKDAY = "weekday"

def segment_data(df: pd.DataFrame, segment: TimeSegment) -> pd.DataFrame:
    """
    Analisa os possíveis outliers dos dados e exibe estatísticas básicas, além de gerar gráficos.

    :param df: DataFrame com os dados carregados
    :param segment: TimeSegment que determina a frequência de segmentação dos dados (dia, hora, minuto, segundo ou dia da semana)
    :return: DataFrame com os dados segmentados ou None em caso de erro
    """
    df = df.copy()
    df.index = pd.to_datetime(df.index)

    try:
        if segment == TimeSegment.WEEKDAY:
            df["timestamp"] = df.index.dayofweek
        else:
            df["timestamp"] = df.index.floor(segment.value)
    except Exception as e:
        print(f'Erro: {e}')
        return None

    grouped_df = df.groupby("timestamp").mean()

    if segment != TimeSegment.WEEKDAY:
        grouped_df["hour"] = grouped_df.index.hour
        grouped_df["minute"] = grouped_df.index.minute
        grouped_df["second"] = grouped_df.index.second
        grouped_df["day_of_month"] = grouped_df.index.day
        grouped_df["day_of_week"] = grouped_df.index.dayofweek
        grouped_df["month"] = grouped_df.index.month
        grouped_df["year"] = grouped_df.index.year

    return grouped_df
