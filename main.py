import pandas as pd

def load_and_validate_csv(file_path: str):
    df = pd.read_csv(file_path)

    total_linhas = len(df)
    print(f"Total de linhas importadas: {total_linhas}")

    inconsistent_rows = df[df.isnull().any(axis=1)].index.tolist()
    if inconsistent_rows:
        print(f"✗ Linhas com número incorreto de colunas: {inconsistent_rows}")
    else:
        print("✓ Todas as linhas possuem o número correto de colunas.")
    
    duplicate_rows_indices = df[df.duplicated()].index.tolist()
    if duplicate_rows_indices:
        print(f"✗ Linhas duplicadas: {duplicate_rows_indices}")
    else:
        print("✓ Nenhuma linha duplicada encontrada.")
    
    return df


def analyze_data(df: pd.DataFrame):
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

def transform_and_save(df: pd.DataFrame, output_file_lstm: str, output_file_transformed: str):
    df_lstm = df[df['attrName'] == 'lstm_forecast']
    if not df_lstm.empty:
        df_lstm_pivot = df_lstm.pivot_table(index='recvTime', columns='attrName', values='attrValue', aggfunc='first')
        df_lstm_pivot = df_lstm_pivot.dropna(axis=1, how='all')
        df_lstm_pivot.to_csv(output_file_lstm)
        print(f"Novo arquivo CSV para 'lstm_forecast' salvo em: {output_file_lstm}")
    
    df_other = df[df['attrName'] != 'lstm_forecast']
    if not df_other.empty:
        df_other_pivot = df_other.pivot_table(index='recvTime', columns='attrName', values='attrValue', aggfunc='first')
        df_other_pivot = df_other_pivot.dropna(axis=1, how='all')
        df_other_pivot.to_csv(output_file_transformed)
        print(f"Novo arquivo CSV para os dados restantes salvo em: {output_file_transformed}")


FILE_PATH = "data.csv"
OUTPUT_FILE_LSTM = "data_lstm.csv"
OUTPUT_FILE_TRANSFORMED = "data_transformed.csv"

print(f"Iniciando analise do arquivo {FILE_PATH}\n")

df = load_and_validate_csv(FILE_PATH)
print()

analyze_data(df)
print()

transform_and_save(df, OUTPUT_FILE_LSTM, OUTPUT_FILE_TRANSFORMED)
print()
