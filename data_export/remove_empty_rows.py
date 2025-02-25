def remove_empty_rows(df, allowed_empty_columns=['timestamp']):
    """
    Remove linhas do DataFrame que contenham qualquer célula vazia, exceto nas colunas permitidas, e retorna o número de linhas removidas.
    
    :param df: DataFrame original
    :param allowed_empty_columns: Lista de colunas que podem ter valores vazios
    :return: DataFrame limpo e número de linhas removidas
    """
    linhas_antes = len(df)
    df_limpo = df.dropna(subset=[col for col in df.columns if col not in allowed_empty_columns])
    linhas_deletadas = linhas_antes - len(df_limpo)
    
    return df_limpo, linhas_deletadas