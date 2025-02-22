import pandas as pd

def analyze_initial_data(df: pd.DataFrame):
    """
    Realiza a analise inicial dos dados, antes das tranformações:
    - Mostra valores DISTINCT entre 'attrName' e 'attrType' se existirem
    - Mostra os valores mínimos e máximos de 'recvTime' se existir

    :param df: DataFrame com os dados carregados
    """
    if 'attrName' in df.columns and 'attrType' in df.columns:
        distinct_combinations = df[['attrName', 'attrType']].dropna().drop_duplicates()
        print("Valores DISTINCT simultâneos entre 'attrName' e 'attrType':")
        print(distinct_combinations.to_string(index=False))
        print("\n")
    
    if 'recvTime' in df.columns:
        min_time = df['recvTime'].min()
        max_time = df['recvTime'].max()
        print(f"Menor valor de 'recvTime': {min_time}")
        print(f"Maior valor de 'recvTime': {max_time}")
        print("\n")

